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

@auth.route('signin', method=['POST'])
def login():
    data = request.get_json()
    User.autheticate(**data)

    if not user:
        return {'message':'Invalid credentials', 'authenticated':False}, 401

    # create JSON Web Token
    token = jwt.encode({
        'sub': user.username,
        'iat': datetime.utcnow(), # time the token was creaeted
        'exp': datetime.utcnow() + timedelta(minutes=30)}
        )