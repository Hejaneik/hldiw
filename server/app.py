from flask import Flask, jsonify, request
from flask_cors import CORS

import datetime

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
