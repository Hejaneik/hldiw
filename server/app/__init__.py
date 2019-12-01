from flask import Flask

app = Flask(__name__)


# avoid circular dependency errors, thus import at bottom
from app import routes