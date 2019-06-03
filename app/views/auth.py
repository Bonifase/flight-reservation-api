from flask import request, jsonify

def home():
    return jsonify("Welcome To Luxurious Flights")