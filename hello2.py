# coding: utf8

from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Index Page</h1>"

@app.route('/login')
def login():
    return "<h1>Login Page</h1>"

@app.route('/user/<username>')
def profile(username):
    return "{}\'s profile" .format(username)

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))