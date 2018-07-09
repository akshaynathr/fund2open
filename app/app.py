from flask import Flask 

app = Flask(__name__)

@app.route('/home')
@app.route('/')
def home():
    return "Welcome to fund to open"