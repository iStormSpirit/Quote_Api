import os

from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if os.environ.get('DATABASE_URL'):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(path, 'test.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False