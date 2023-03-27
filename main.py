from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/hi')
def hello_world():
    return 'Hello, I am CHarLes SuN!'