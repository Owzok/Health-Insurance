from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_seasurf import SeaSurf
from flask_talisman import Talisman
from twilio.rest import Client
from datetime import timedelta
app = Flask(__name__)
#csrf = SeaSurf(app)
Talisman(app, force_https=True)

TWILIO_SID = 'ACd0fd6aa1a357d13a965b67f1a1f6e895'
TWILIO_AUTH_TOKEN = 'ae6360cb35071e7b87bc595eef546e99'

twilio_client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

app.config['SECRET_KEY'] = 'alanmorante'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:fubuki00@esd-basedatos-mysql.cfojfplxkq0l.us-east-1.rds.amazonaws.com:3306/proyesd'
app.config['CSRF_DISABLE'] = True 

app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)

CORS(app, origin=['http://127.0.0.1:5000'])

db = SQLAlchemy(app)
jwt = JWTManager(app)

from flaskapp import routes