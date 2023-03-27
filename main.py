from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/login')
def login():
    return 'Login'

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username
    