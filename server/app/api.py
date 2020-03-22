# API blueprint

from flask import Blueprint, jsonify, request
from datetime import datetime
import uuid

from .models import Delay, DelaySchema, User, UserSchema
from .auth import token_required
from . import db, ma

api = Blueprint('api', __name__)

user_schema = UserSchema()
users_schema = UserSchema(many=True)
delay_schema = DelaySchema()
delays_schema = DelaySchema(many=True)


# route to check if server responds
@api.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong')

# route to add a single delay
# TODO handle users and make GET route for single delay (TODO is this needed/useful)
@api.route('/delay', methods=['POST'])
@token_required
def add_delay():
    post_data = request.get_json()
    datetime_obj = datetime.strptime(
        post_data.get('date'), '%Y-%m-%dT%H:%M:%S.%fZ')
    new_delay = Delay(1, 2, post_data.get('delay'),
                      datetime_obj, post_data.get('excuse'))
    db.session.add(new_delay)
    db.session.commit()
    return delay_schema.jsonify(new_delay)

# route to get all delays
# TODO add ID for user to only get specific delays/ add other options
@api.route('/delays', methods=['GET', 'POST'])
def all_delays():
    return delays_schema.jsonify(Delay.query.all())

# route to GET a single user and POST to alter user data (TODO needs authentication)
@api.route('/user/<user_id>', methods=['GET', 'POST'])
def user(user_id):
    if request.method == 'GET':
        return user_schema.jsonify(User.query.filter_by(id=user_id).first())
    if request.method == 'POST':
        pass
        # TODO

# route to get all friends of specfic user
@api.route('/friends', methods=['GET'])
@token_required
def friends():
    return users_schema.jsonify(User.query.all())
