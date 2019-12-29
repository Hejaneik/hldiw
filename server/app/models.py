from datetime import datetime
import uuid

from . import db, ma


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=True)
    password = db.Column(db.String(120), nullable=False)
    user_since = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
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


class Delay(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    late_person_id = db.Column(
        db.Integer, db.ForeignKey('user.id'), nullable=False)
    # to resolve dependency issues
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
        fields = ('id', 'owner_id', 'late_person_id',
                  'delay', 'date', 'excuse')
