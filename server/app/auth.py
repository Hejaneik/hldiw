# auth blueprint

from flask import Blueprint, jsonify, request, current_app
from datetime import datetime, timedelta
from functools import wraps
import logging

import jwt

from . import db, ma
from .models import User, UserSchema

auth = Blueprint('auth', __name__)

user_schema = UserSchema()

# route to add a user
@auth.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    current_app.logger.error("User Data", data)
    user = User.query.filter((User.email == data.email) | (User.username == data.username)).first()
    if user:
        return None, 406 # TODO flash correct error message

    user = User(**data)
    db.session.add(user)
    db.session.commit()
    return user_schema.jsonify(user), 201

# route to sign in a user
@auth.route('/signin', methods=['POST'])
def login():
    data = request.get_json()
    user = User.authenticate(**data)

    if not user:
        return {'message':'Invalid credentials', 'authenticated':False}, 401

    # create JSON Web Token
    token = jwt.encode({
        'sub': user.username,
        'iat': datetime.utcnow(), # time the token was created
        'exp': datetime.utcnow() + timedelta(minutes=30)},
        current_app.config['SECRET_KEY'])
        
    return jsonify({'token': token.decode('UTF-8')})

def token_required(f):
    @wraps(f)
    def _verify(*args, **kwargs):
        auth_headers = request.headers.get('Authorization', '').split()

        invalid_msg = {
            'message': 'Invalid token. Registration and/or reauthetication required',
            'authenticated': False
        }
        expired_msg = {
            'message': 'Token expried, reauthetication required',
            'authenticated': False
        }

        if len(auth_headers) != 2:
            return jsonify(invalid_msg), 401
        
        try:
            token = auth_headers[1]
            data = jwt.decode(token, current_app.config['SECRET_KEY'])
            user = User.query.filter_by(username=data['sub']).first()
            if not user:
                raise RuntimeError('User not found')
            return f(user, *args, **kwargs) # TODO check this
        except jwt.ExpiredSignatureError:
            return jsonify(expired_msg), 401
        except (jwt.InvalidTokenError, Exception) as e:
            print(e)
            return jsonify(invalid_msg), 401

    return _verify