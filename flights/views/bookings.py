import datetime
from flights import app
from flask import request, jsonify
from flask_jwt_extended import (jwt_required, get_jwt_identity)

from flights.models.flight import Flight, Seat
from flights.models.bookings import Booking
from validators.validator import validate_data
from helpers.check_existing_booking import check_available_slot


@app.route('/api/booking', methods=['POST'])
@jwt_required
def create_booking():
    user = get_jwt_identity()
    data = request.get_json()
    booking = {
        'flight_name': data.get('flight_name'),
        'seat_number': data.get('seat_number'),
        'payment': data.get('payment')
        }
    try:
        cleaned_data = validate_data(**booking)
    except AssertionError as error:
        return jsonify({'error': error.args[0]}), 409
    
    if cleaned_data:
        exact_flight = Flight.query.filter_by(
            name=data['flight_name']).first()
        exact_seat = Seat.query.filter_by(
        number=data['seat_number']).first()
        try:
            check_available_slot(user, cleaned_data, exact_flight, exact_seat)
        except AssertionError as error:
            return jsonify({'error': error.args[0]}), 409
        booking = Booking(
            user,
            cleaned_data["flight_name"], 
            cleaned_data["seat_number"],
            cleaned_data["payment"],
            date_booked=datetime.datetime.now()
            )
        booking.save_booking()
        exact_seat.booked = True
        exact_seat.save_seat()
    
        response = {
                '_id': booking.id,
                'flight': booking.flight_name,
                'seat': booking.seat_number,
                'payment': booking.payment,
                'date_booked': booking.date_booked,
                'departure': exact_flight.departure,
                'destination': exact_flight.destination,
                'user_id': user,
                }

    return jsonify(
        {
            "message": "You Booked sucessfully",
            "flight": response}), 201

@app.route('/api/booking', methods=['GET'])
@jwt_required
def get_bookings():
    user = get_jwt_identity()
    bookings = Booking.query.all()
    user_bookings = [
        {
            '_id': booking.id,
            'flight': booking.flight_name,
            'seat': booking.seat_number,
            'payment': booking.payment,
            'date_booked': booking.date_booked,
            'user_id': user} for booking in bookings if booking.user_id == user]
    return jsonify({"bookings": user_bookings}), 200