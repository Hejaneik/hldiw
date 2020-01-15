# auth blueprint

from flask import Blueprint, jsonify, request
from datetime import datetime

import jwt

from . import db, ma
from .models import User, UserSchema

auth = Blueprint('auth', __name__)

user_schema = UserSchema()

# routes will go here
@auth.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()

    user = User.query.filter((User.email == data.email) | (User.username == data.username)).first()
    if user:
        return None, 406 # TODO flash correct error message

    user = User(**data)
    db.session.add(user)
    db.session.commit()
    return user_schema.jsonify(user), 201