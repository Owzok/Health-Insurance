from flask import Flask, render_template, request, send_from_directory, Response, redirect
from flaskapp import app

@app.route('/')
def hello_world():
    return render_template('index.html')