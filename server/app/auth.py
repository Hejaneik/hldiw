# auth blueprint

from flask import Blueprint
from . import db, ma

auth = Blueprint('auth', __name__)

# routes will go here