from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager

app = Flask(__name__)

app.config['SECRET_KEY'] = 'alanmorante'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:fubuki00@esd-basedatos-mysql.cfojfplxkq0l.us-east-1.rds.amazonaws.com:3306/proyesd'

CORS(app, origin=['http://127.0.0.1:5000'])

db = SQLAlchemy(app)
jwt = JWTManager(app)

from flaskapp import routes