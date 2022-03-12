from flask import Flask
from scraper import module

app = Flask(__name__)

@app.route('/')
def index():
    return "This is a sample flask Web App! <h1>HELLO<h1>"
