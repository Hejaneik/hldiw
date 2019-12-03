from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime

# configuration
DEBUG = True

RECORDS = [
    {
        'name': 'Max Mustermann',
        'time': '2 hours',
        'date': datetime.datetime(2019, 12, 2),
        'excuse': 'none'
    },
    {
        'name': 'Max Mustermann',
        'time': '3 hours',
        'date': datetime.datetime(2019, 12, 3),
        'excuse': 'laziness'
    },
    {
        'name': 'Mux Mastermann',
        'time': '2 hours',
        'date': datetime.datetime(2019, 12, 1),
        'excuse': 'Shopping in airsoft shop'
    }
]

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp/test.db'
db = SQLAlchemy(app)

# model database tables
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=True)
    password = db.Column(db.String(120), nullable=False)
    user_since = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    email = db.Column(db.String(120), nullable=False)
    posts = db.relationship('Delays', backref='user', lazy=True)

    def __repr__(self):
        return f'User({username}, {first_name}, {last_name})'

admin = User(username='admin', first_name='Hendrik', last_name='Hoefert', password='admin', email='admin@example.com')
lucas = User(username='cpastoncp', first_name='Lucas', last_name='Jansen', paswwort='password', email='lucasjansen@example.com')

class Delays(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    late_person_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    #to resolve dependency issues
    owner = db.relationship('User', foreign_keys=[owner_id])
    late_person = db.relationship('User', foreign_keys=[late_person_id])
    delay = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    excuse = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'Delay({owner}, {late_person}, {delay}, {date})'

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong')


@app.route('/records', methods=['GET', 'POST'])
def all_records():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        RECORDS.append({
            'name': post_data.get('name'),
            'time': post_data.get('time'),
            'date': post_data.get('date'),
            'excuse': post_data.get('excuse'),
        })
        response_object['message'] = 'Record added'
    else:
        response_object['records'] = RECORDS
    return jsonify(response_object)


if __name__ == '__main__':
    app.run()
