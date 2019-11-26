from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

# Security
app.config['SECRET_KEY'] = '2a7a0aab1f222297928e17a5d00a0eae'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users_base.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from application import routes
