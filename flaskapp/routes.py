from flask import render_template, request, redirect, url_for, jsonify, make_response, session
from flaskapp import app, db, jwt, limiter
import uuid
from users import User, FailedLoginAttempt
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
import random
from datetime import datetime, timedelta

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
    access_token = session.get('access_token')
    username = session.get('username')
    if access_token and username:
        return render_template("index.html")
        response = make_response(render_template('main.html', username=username))
        response.set_cookie('access_token', value=access_token, secure=True, httponly=True, samesite='Strict')
        return response
    return render_template('index.html')

MAX_FAILED_ATTEMPTS = 3
TIME_WINDOW = timedelta(minutes=15)
LOCKOUT_DURATION = timedelta(minutes=30)

def lock_account(username):
    user = User.query.filter_by(username=username).first()
    user.locked = True
    user.locked_until = datetime.now() + LOCKOUT_DURATION
    db.session.commit()

def check_account_lock(username):
    user = User.query.filter_by(username=username).first()
    if user.locked:
        if user.locked_until and user.locked_until <= datetime.now():
            unlock_account(username)
        else:
            return True
    return False

def unlock_account(username):
    user = User.query.filter_by(username=username).first()
    user.locked = False
    user.locked_until = None
    db.session.commit()

@app.route('/login', methods=['POST'])
@limiter.limit("5 per 5 minutes")
def login():
    username = request.form['username']
    password = request.form['password']

    # Falta cambiar la BD
    #if check_account_lock(username):
    #    return "Account is locked. Please try again later."

    user = User.query.filter_by(username=username).first()

    if user and user.check_password(password):
        access_token = create_access_token(identity=user.id)

        session['access_token'] = access_token
        session['username'] = username

        response = make_response(render_template('main.html', username=user.username))
        response.set_cookie('access_token', value=access_token, secure=True, httponly=True, samesite='Strict')
        return response

    failed_attempt = FailedLoginAttempt(username=username, timestamp=datetime.now())
    db.session.add(failed_attempt)
    db.session.commit()

    recent_attempts = FailedLoginAttempt.query.filter(
            FailedLoginAttempt.username == username,
            FailedLoginAttempt.timestamp >= datetime.now() - TIME_WINDOW
        ).count()

    if recent_attempts >= MAX_FAILED_ATTEMPTS:
        lock_account(username)
        return "Account is locked. Please try again later."
    else:
        print("Login Failed 401")
        return render_template("index.html")
    

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        nrotelf = request.form['nrotelf']

        if User.query.filter_by(username=username).first() is not None:
            username_taken = True
        else:
            new_user = User(username=username, password=password, nrotelf=nrotelf)
            db.session.add(new_user)
            db.session.commit()
            return render_template("index.html")
    else:
        username_taken = False
    return render_template('register.html', username_taken=username_taken)

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
    print(session)
    session.clear()
    print(session)
    return redirect(url_for('index'))
