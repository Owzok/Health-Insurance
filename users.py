from flaskapp import app, db
from flask_jwt_extended import create_access_token
import bcrypt

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    SSN = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    blocked = db.Column(db.Boolean, nullable=False)

    def __init__(self, name, surname, password, SSN, email, blocked):
        self.name = name
        self.surname = surname
        self.password = self.hash_password(password)
        self.SSN = SSN
        self.email = email
        self.blocked = blocked

    def hash_password(self, password):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))
    
    def create_token(self):
        return create_access_token(identity=self.id)

class Insurance(db.Model):
    __tablename__ = 'insurance'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, unique=True, nullable=False)
    insurance_id = db.Column(db.String(100), unique=True, nullable=False)
    previously_insured = db.Column(db.Boolean, nullable=False)
    vintage = db.Column(db.Integer)
    response = db.Column(db.Boolean, nullable=False)

    def __init__(self, user_id, insurance_id, previously_insured, vintage, response):
        self.user_id = user_id
        self.insurance_id = insurance_id
        self.previously_insured = previously_insured
        self.vintage = vintage
        self.response = response

class Vehicle(db.Model):
    __tablename__ = 'vehicles'

    vehicle_id = db.Column(db.String(100), primary_key=True)
    user_id = db.Column(db.Integer, unique=True, nullable=False)
    brand = db.Column(db.String(20), nullable=False)
    model = db.Column(db.String(30), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    car_vin = db.Column(db.String(100), unique=True, nullable=False)
    use_place = db.Column(db.String(100), nullable=False)

    def __init__(self, user_id, vehicle_id, brand, model, year, car_vin, use_place):
        self.user_id = user_id
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.model = model
        self.year = year
        self.car_vin = car_vin
        self.use_place = use_place

class FailedLoginAttempt(db.Model):
    __tablename__ = 'failed_login_attempts'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.TIMESTAMP, nullable=False)

    def __init__(self, user_id, timestamp):
        self.user_id = user_id
        self.timestamp = timestamp