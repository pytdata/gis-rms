from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1><span style="color:red;">Hello World!</span></h1>'