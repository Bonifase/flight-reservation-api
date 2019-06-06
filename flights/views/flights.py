from flights import app
from flask import request, jsonify
from flask_jwt_extended import (jwt_required, get_jwt_identity,
    create_access_token,  decode_token, get_raw_jwt
)

from flights.models.flight import Flight, Seat
from validators.validator import validate_data


@app.route('/api/flight', methods=['POST'])
@jwt_required
def create_flight():
    user = get_jwt_identity()
    data = request.get_json()
    flight = {'name': data.get('name'), 'departure': data.get('departure'),
    'arrival': data.get('arrival'), 'destination': data.get('destination')}
    try:
        cleaned_data = validate_data(**flight)
    except AssertionError as error:
        return jsonify({'error': error.args[0]}), 409
    
    if cleaned_data:
        
        available_names = [
            flight.name.lower() for flight in Flight.get_flights()]    
        if cleaned_data['name'].lower() in available_names:
            return jsonify(
                {"error": "Flight already Exist, use another name"}), 409
        else:
            try:
                flight = Flight(
                    cleaned_data["name"], cleaned_data["departure"],
                    cleaned_data["arrival"],
                    cleaned_data["destination"])
                flight.save_flight()
            except AssertionError as err:
                return jsonify({"error": err.args[0]}), 409

            response = {
                '_id': flight.id,
                'Name': flight.name,
                'Departure': flight.departure,
                'arrival': flight.arrival,
                'destination': flight.destination}

    return jsonify(
        {
            "message": "You created a new flight",
            "flight": response}), 201

@app.route('/api/flights', methods=['GET'])
def view_flights():
    flights = [{
        '_id': flight.id, 
        'Name': flight.name,
        'Departure' : "{:%Y-%m-%d %H:%M}".format(flight.departure),
        'arrival': "{:%Y-%m-%d %H:%M}".format(flight.arrival),
        'destination': flight.destination} for flight in Flight.get_flights()]
    if flights == [{}]:
        return jsonify({"message": "No Flight Entry"}), 404
    else:
        return jsonify({"flights": flights}), 200

@app.route('/api/<int:flight_id>/seats', methods=['POST'])
@jwt_required
def create_seat(flight_id):
    data = request.get_json()
    seat = {'number' : data.get('number')}
    try:
        cleaned_data = validate_data(**seat)
    except AssertionError as error:
        return jsonify({'error': error.args[0]}), 409
    if cleaned_data:
        target_flight = Flight.query.filter_by(id=flight_id).first()
        if target_flight:
            number = cleaned_data.get('number') + target_flight.name[:2].upper()
            existing_seat = Seat.query.filter_by(number=number).first()
            if existing_seat:
                return jsonify({'error': "That seat number has been added"}), 409
            seat = Seat(number, flight_id, booked=False)
            seat.save_seat()
            return jsonify({"message": "Seat added Successfully"}), 201
        else:
            return jsonify({
                "message": "Flight with that ID does not exist"}), 404

@app.route('/api/<int:flight_id>/seats', methods=['GET'])
def get_seats(flight_id):
    seats = Seat.query.all()
    target_seats = [
        {"_id": seat.id,
            "flight_id": seat.flight_id,
            "booked": seat.booked,
            "number": seat.number} for seat in seats if seat.flight_id == flight_id]
    if target_seats == [{}]:
        return jsonify({
            "message": "No Seats available for that Flight"}), 404
    else:
        return jsonify({"seats": target_seats}), 200