# coding: utf8

from flask import Flask

app = Flask(__name__)

@app.route('/')
def Index():
    return "<h1>Index Page</h1>"

@app.route('/hello')
def Hello():
    return "<h1>Hello world!</h>"

@app.route('/firstpage')
def firstpage():
    return "<h1>This is first page.<h1>"

@app.route('/secondpage')
def secondpage():
    return "<h1>This is second page.</h1>"

@app.route('/user/<username>')
def show_user_profile(username):
    return "Hi, %s" % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return "Post %d" % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return "Subpath %s" % subpath

@app.route('/projects/')
def projects():
    return "<h1>The project page</h1>"

@app.route('/about')
def about():
    return "<h1>The about page</h1>"