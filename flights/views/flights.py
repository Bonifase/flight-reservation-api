from flights import app
from flask import render_template
from flask_jwt_extended import jwt_required

from flights.controller.flight_controller import FlightController

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/flight', methods=['POST'])
@jwt_required
def create_flight():

    return FlightController.create()

@app.route('/api/flight/<int:flight_id>', methods=['PUT'])
@jwt_required
def update_flight(flight_id):

    return FlightController.update(flight_id)

@app.route('/api/flight/<int:flight_id>', methods=['DELETE'])
@jwt_required
def delete_flight(flight_id):

    return FlightController.delete(flight_id)
    

@app.route('/api/flights', methods=['GET'])
def view_flights():
    
    return FlightController.flights()

@app.route('/api/<int:flight_id>/seats', methods=['POST'])
@jwt_required
def create_seat(flight_id):
    
     return FlightController.create_seat(flight_id)

@app.route('/api/<int:flight_id>/seats/<int:seat_id>', methods=['PUT'])
@jwt_required
def update_seat(flight_id, seat_id):
    
    return FlightController.update_seat(flight_id, seat_id)

@app.route('/api/<int:flight_id>/seats/<int:seat_id>', methods=['DELETE'])
@jwt_required
def delete_seat(flight_id, seat_id):
   
    return FlightController.delete_seat(flight_id, seat_id)

@app.route('/api/<int:flight_id>/seats', methods=['GET'])
def get_seats(flight_id):
    
    return FlightController.seats(flight_id)