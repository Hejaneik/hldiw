from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import uuid

from datetime import datetime

# configuration
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp/test.db'
app.config['CORS_HEADERS'] = 'Content-Type'

db = SQLAlchemy(app)
ma = Marshmallow(app)

# model database tables
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=True)
    password = db.Column(db.String(120), nullable=False)
    user_since = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    email = db.Column(db.String(120), nullable=False)
    # posts = db.relationship('Delays', backref='user', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.first_name}', '{self.last_name}')"

    def __init__(self, username, first_name, last_name, password, email, user_since):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.email = email
        self.user_since = user_since
        # self.id = uuid.uuid4().int

admin = User(username='admin', first_name='Hendrik', last_name='Hoefert', password='admin', email='admin@example.com', user_since=datetime.utcnow())
lucas = User(username='cpastoncp', first_name='Lucas', last_name='Jansen', password='password', email='lucasjansen@example.com', user_since=datetime.utcnow())

class Delay(db.Model):
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
        return f'Delay({self.owner}, {self.late_person}, {self.delay}, {self.date}, {self.excuse})'

    def __init__(self, owner_id, late_person_id, delay, date, excuse):
        self.owner_id = owner_id
        self.late_person_id = late_person_id
        self.delay = delay
        self.date = date
        self.excuse = excuse
        # self.id = uuid.uuid4().int

# Initialize schemas
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'first_name', 'last_name', 'user_since')

class DelaySchema(ma.Schema):
    class Meta:
        fields = ('id', 'owner_id', 'late_person_id', 'delay', 'date', 'excuse')

user_schema = UserSchema()
users_schema = UserSchema(many=True)
delay_schema = DelaySchema()
delays_schema = DelaySchema(many=True)


# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# route to check if server responds
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong')

# route to add a single delay
# TODO handle users and make GET route for single delay (TODO is this needed/useful)
@app.route('/delay', methods=['POST'])
def add_delay():
    post_data = request.get_json()
    datetime_obj = datetime.strptime(post_data.get('date'), '%Y-%m-%dT%H:%M:%S.%fZ')
    new_delay = Delay(1, 2, post_data.get('delay'), datetime_obj, post_data.get('excuse'))
    db.session.add(new_delay)
    db.session.commit()
    return delay_schema.jsonify(new_delay)

# route to get all delays
# TODO add ID for user to only get specific delays/ add other options
@app.route('/delays', methods=['GET', 'POST'])
def all_delays():
    return delays_schema.jsonify(Delay.query.all())

# route to GET a single user and POST to alter user data (TODO needs authentication)
@app.route('/user/<user_id>', methods=['GET', 'POST'])
def user(user_id):
    if request.method == 'GET':
        return user_schema.jsonify(User.query.filter_by(id=user_id).first())
    if request.method == 'POST':
        pass
        # TODO

# route to get all friends of specfic user
@app.route('/friends', methods=['GET'])
def friends():
    return users_schema.jsonify(User.query.all())

if __name__ == '__main__':
    app.run()
