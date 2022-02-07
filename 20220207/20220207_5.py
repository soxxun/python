# light web server
from flask import Flask
app = Flask(__name__)

@app.route("/test")
def hello():
    return "<h1>Weather News</h1>"

@app.route("/")
def hello2():
    return "<h1>Welcome home</h1>"

# open Terminal
#set FLASK_APP=파일.py
#flask run