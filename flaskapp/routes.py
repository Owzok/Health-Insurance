from flask import render_template, request, redirect, url_for, jsonify
from flaskapp import app, db, jwt
import uuid
from users import User
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    user = User.query.filter_by(username=username).first()

    if user and user.check_password(password):
        access_token = create_access_token(identity=user.id)
        print({'access_token': access_token}, 200)
        return render_template('main.html', username=user.username)

    return 'Login Failed', 401

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if User.query.filter_by(username=username).first() is not None:
            username_taken = True
        else:
            new_user = User(username=username, password=password)
            db.session.add(new_user)
            db.session.commit()
            return 'Registration successful'
    else:
        username_taken = False
    return render_template('register.html', username_taken=username_taken)

@app.route('/protected', methods=['GET'])
#@jwt.required()
def protected_route():
    current_user_id = get_jwt_identity()
    return f'Protected route accessed by {current_user_id}'