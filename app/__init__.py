from flask import Flask, jsonify
from app.views import auth

app = Flask(__name__)

@app.route('/') 
def index():
    response = auth.home()
    return response
