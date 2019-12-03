from flask import Flask, jsonify
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


@app.route('/records', methods=['GET'])
def all_records():
    return jsonify({
        'status': 'success',
        'records': RECORDS
    })


if __name__ == '__main__':
    app.run()
