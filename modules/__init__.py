from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = '4YrzfpQ4kGXjuP6w'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////mnt/c/Users/R23M/Documents/twitter-clone/modules/database.db'

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'home'
socketio = SocketIO(app)

from modules import routes
