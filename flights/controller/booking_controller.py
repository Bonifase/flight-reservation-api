import datetime
from flask import request, jsonify
from flask_jwt_extended import (get_jwt_identity)

from flights.models.flight import Flight, Seat
from flights.models.bookings import Booking
from validators.validator import validate_data
from helpers.check_existing_booking import check_available_slot
from helpers.check_admin_user import *


class BookingController:
    """Controls all bookings and those of each flight"""

    def create():
        """creat booking objects for logged in users"""

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
            try:
                flight, seat = check_available_slot(user, cleaned_data)
            except AssertionError as error:
                return jsonify({'error': error.args[0]}), 409
            booking = Booking(
                user_id=user,
                flight_name=cleaned_data["flight_name"], 
                seat_number=cleaned_data["seat_number"], 
                payment=cleaned_data["payment"],
                date_booked=datetime.datetime.now()
                )
            booking.save_booking()
            seat.booked = True
            seat.save_seat()
        
            response = {
                    '_id': booking.id,
                    'flight': booking.flight_name,
                    'seat': booking.seat_number,
                    'payment': booking.payment,
                    'date_booked': booking.date_booked,
                    'departure': flight.departure,
                    'destination': flight.destination,
                    'user_id': user,
                    }

        return jsonify(
            {
                "message": "You Booked sucessfully",
                "flight": response}), 201

    def bookings():
        """Returns all the bookings of a specific user"""

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

    def flight_bookings(flight_id):
        """"Returns all the flight bookings"""

        user_id = get_jwt_identity()
        user = get_user(user_id)
        try:
            flight = get_flight(flight_id)
        except AssertionError as error:
            return jsonify({'error': error.args[0]}), 404
        bookings = Booking.query.all()
        user_bookings = [
            {
                '_id': booking.id,
                'flight': booking.flight_name,
                'seat': booking.seat_number,
                'payment': booking.payment,
                'departure': flight.departure,
                'arrival': flight.arrival,
                'destination': flight.destination,
                'user': user.username} for booking in bookings if booking.flight_name == flight.name]
        return jsonify({"flight_bookings": user_bookings}), 200