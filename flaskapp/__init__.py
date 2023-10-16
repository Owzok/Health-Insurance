from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_seasurf import SeaSurf
from flask_talisman import Talisman
from datetime import timedelta
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)
#csrf = SeaSurf(app)
Talisman(app, force_https=True)
limiter = Limiter(get_remote_address, app=app, default_limits=["200 per day", "50 per hour"], storage_uri="memory://")

app.config['SECRET_KEY'] = 'alanmorante'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:fubuki00@esd-basedatos-mysql.cfojfplxkq0l.us-east-1.rds.amazonaws.com:3306/proyesd'
#app.config['CSRF_DISABLE'] = True 

app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)

CORS(app, origin=['http://127.0.0.1:5000'])

db = SQLAlchemy(app)
jwt = JWTManager(app)

from flaskapp import routes