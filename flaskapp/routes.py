from flask import render_template, request, redirect, url_for, jsonify, make_response, session
from flaskapp import app, db, jwt, limiter
import uuid
from users import User, FailedLoginAttempt, Vehicle
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
import random
from datetime import datetime, timedelta
import smtplib
from email.message import EmailMessage
from cryptography.fernet import Fernet
import rsa
from cryptography.hazmat.primitives import serialization


def generate_verification_code(length=6):
    return "123456"






def is_code_expired(created_at, expiry_minutes=5):
    current_time = datetime.now()
    created_time = datetime.strptime(created_at, '%Y-%m-%d %H:%M:%S')
    expiration_time = created_time + timedelta(minutes=expiry_minutes)
    return current_time > expiration_time







def send_email(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = 'martsmtplib@gmail.com'
    password = 'uvbvmykzhwjvpnpk'

    msg['from'] = user
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)

    server.quit()






def log_error(exception):
    # mejorar eso
    error_data = {
        "error_message": str(exception),
        "request_path": request.path,
        "user_agent": request.user_agent.string,
    }
    # send it to a db





@app.errorhandler(404)
def not_found_error(error):
    log_error(error) 
    return render_template('404.html'), 404





@app.errorhandler(500)
def internal_error(error):
    log_error(error)
    return render_template('500.html'), 500






@app.route('/')
def index():


    data = "Sensitive data to be encrypted"
    data_key = decrypt_data_key()
    encrypted_data = encrypt_data(data, data_key)
    decrypted_data = decrypt_data(encrypted_data, data_key)
    print(data, "\n", encrypted_data, "\n",decrypted_data)

    encrypted_data = encrypt_data(data, data_key)
    decrypted_data = decrypt_data(encrypted_data, data_key)
    print(data, "\n", encrypted_data, "\n",decrypted_data)


    access_token = session.get('access_token')
    username = session.get('username')
    if access_token and username:
        return redirect(url_for('main'))

    return render_template('index.html')






MAX_FAILED_ATTEMPTS = 3
TIME_WINDOW = timedelta(minutes=15)
LOCKOUT_DURATION = timedelta(minutes=30)






def lock_account(email):
    user = User.query.filter_by(email=email).first()
    user.locked = True
    user.locked_until = datetime.now() + LOCKOUT_DURATION
    db.session.commit()






def check_account_lock(email):
    user = User.query.filter_by(email=email).first()
    if user.locked:
        if user.locked_until and user.locked_until <= datetime.now():
            unlock_account(username)
        else:
            return True
    return False






def unlock_account(email):
    user = User.query.filter_by(email=email).first()
    user.locked = False
    user.locked_until = None
    db.session.commit()






@app.route('/main', methods=['GET'])
@jwt_required(optional=True)
def main():
    print(request.headers)
    if 'access_token' in session:
        #current_user_id = get_jwt_identity()
        #print(current_user_id)
        username = session.get('username')
        #user = User.query.filter_by(id=current_user_id).first()
        print(session.get('id'))
        vehicles = Vehicle.query.filter_by(user_id=session.get('id')).all()
        print(vehicles)
        return render_template('main.html', username=username, vehicles=vehicles)
        return render_template('main.html', username=session.get('username'))
    else:
        return redirect(url_for('index'))






# para encriptar/desencriptar abrimos la RSA y desencriptamos data_key


def decrypt_data_key():
    with open("./flaskapp/keys/PrivateKeyRSA.pem", 'rb') as f:
        private_key_data = f.read()
        private_key = rsa.PrivateKey.load_pkcs1(private_key_data)
    
    with open("./flaskapp/keys/Data_key_encrypted.sym", 'rb') as f:
        data_key_encrypted = f.read()

    data_key = rsa.decrypt(data_key_encrypted, private_key)
    return data_key

def encrypt_data(data, data_key):
    f = Fernet(data_key)
    encrypted_data = f.encrypt(data.encode()).decode()
    return encrypted_data

def decrypt_data(encrypted_data, data_key):
    f = Fernet(data_key)
    decrypted_data = f.decrypt(encrypted_data.encode()).decode()
    return decrypted_data





@app.route('/login', methods=['POST'])
@limiter.limit("5 per 5 minutes")
def login():
    data_key = decrypt_data_key()

    email = request.form['email']
    password = request.form['password']

    # Falta cambiar la BD
    #if check_account_lock(username):
    #    return "Account is locked. Please try again later."

    user = User.query.filter_by(email=email).first()

    if user and user.check_password(password):
        access_token = create_access_token(identity=user.id)

        verification_code = generate_verification_code()
        created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        send_email("Login successful", verification_code, "pajjarittoss@gmail.com")
        #print(is_code_expired(created_at))

        username = decrypt_data(user.name, data_key) + " " + decrypt_data(user.surname, data_key)

        session['access_token'] = access_token
        session['username'] = username
        session['id'] = user.id

        response = make_response(redirect(url_for('main')))
        response.set_cookie('access_token', value=access_token, secure=True, httponly=True, samesite='Strict')
        response.headers['Authorization'] = f'Bearer {access_token}'
        return response

    failed_attempt = FailedLoginAttempt(user_id=user.id, timestamp=datetime.now())
    db.session.add(failed_attempt)
    db.session.commit()

    recent_attempts = FailedLoginAttempt.query.filter(
            FailedLoginAttempt.user_id == user.id,
            FailedLoginAttempt.timestamp >= datetime.now() - TIME_WINDOW
        ).count()

    if recent_attempts >= MAX_FAILED_ATTEMPTS:
        lock_account(email)
        return "Account is locked. Please try again later."
    else:
        print("Login Failed 401")
        return render_template("index.html")
    









@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        password = request.form['password']
        SSN = request.form['SSN']
        email = request.form['email']

        data_key = decrypt_data_key()

        if User.query.filter_by(email=email).first() is not None:
            email_taken = True
        else:
            new_user = User(name=encrypt_data(name, data_key), surname=encrypt_data(surname, data_key), password=password, SSN=encrypt_data(SSN, data_key), email=email, blocked=False)
            db.session.add(new_user)
            db.session.commit()
            return render_template("index.html")
    else:
        email_taken = False
    return render_template('register.html', email_taken=email_taken)

    #data = "Sensitive data to be encrypted"
    #data_key = decrypt_data_key()
    #encrypted_data = encrypt_data(data, data_key)
    #decrypted_data = decrypt_data(encrypted_data, data_key)
    #print(data, "\n", encrypted_data, "\n",decrypted_data)









@app.route('/protected', methods=['GET'])
@jwt_required(optional=True)
def protected_route():
    access_token = session.get('access_token')
    username = session.get('username')
    if access_token and username:
        return f'Protected route accessed by user with ID {username}'
    else:
        return 'Unauthorized', 401








@app.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return redirect(url_for('index'))
