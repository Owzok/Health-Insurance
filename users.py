from flaskapp import app, db
from flask_jwt_extended import create_access_token
import bcrypt

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    nrotelf = db.Column(db.String(12), unique=True, nullable=False)
    #token = db.Column(db.String(128), unique=True)

    def __init__(self, username, password, nrotelf):
        self.username = username
        self.password = self.hash_password(password)
        self.nrotelf = nrotelf
        #self.token = None

    def hash_password(self, password):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))
    
    def create_token(self):
        return create_access_token(identity=self.id)