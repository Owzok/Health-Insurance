from flask import render_template, request, redirect, url_for, jsonify, make_response, session
from flaskapp import app, db, jwt, twilio_client
import uuid
from users import User
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
import random

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

@app.route('/')
def index():
    access_token = session.get('access_token')
    username = session.get('username')
    if access_token and username:
        response = make_response(render_template('main.html', username=username))
        response.set_cookie('access_token', value=access_token, secure=True, httponly=True, samesite='Strict')
        return response
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    user = User.query.filter_by(username=username).first()

    if user and user.check_password(password):
        access_token = create_access_token(identity=user.id)

        session['access_token'] = access_token
        session['username'] = username

        response = make_response(render_template('main.html', username=user.username))
        response.set_cookie('access_token', value=access_token, secure=True, httponly=True, samesite='Strict')
        return response
    
    return 'Login Failed', 401

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
            return 'Registration successful'
    else:
        username_taken = False
    return render_template('register.html', username_taken=username_taken)

@app.route('/protected', methods=['GET'])
@jwt_required(optional=True)
def protected_route():
    current_user_id = get_jwt_identity()
    if current_user_id:
        return f'Protected route accessed by user with ID {current_user_id}'
    elif 'access_token' in request.cookies:
        return f'Protected route accessed by user with token in cookies'
    else:
        return 'Unauthorized', 401
    

@app.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return redirect(url_for('index'))
