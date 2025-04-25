from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

db = SQLAlchemy()

app = Flask(__name__)

login_manager = LoginManager()

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# This will default users to the login page
# Then they will need proper credentials to access the rest of the site
login_manager.init_app(app)
login_manager.login_view = 'login'

with app.app_context():
    from . import routes
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    from .models import User
    return User.query.get(int(user_id))
