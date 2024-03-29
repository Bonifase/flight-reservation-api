from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity

from flights.models.flight import Flight, Seat
from validators.validator import validate_data
from helpers.check_admin_user import check_admin_user
from helpers.send_email import send_email
from helpers.create_object import (flight_object, create_response_obj,
                                   serialize_flights)


class FlightController:
    """Controls the flow of data between flight models"""

    def create():
        """Takes data from request object
        validates the data
        saves the data to database
        """
        user = get_jwt_identity()
        try:
            check_admin_user(user)
        except AssertionError as error:
            return jsonify({'error': error.args[0]}), 403
        data = request.get_json()
        flight = flight_object(data)
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
                        cleaned_data["name"],
                        cleaned_data["departure"],
                        cleaned_data["arrival"],
                        cleaned_data["destination"])
                    flight.save_flight()
                except AssertionError as err:
                    return jsonify({"error": err.args[0]}), 409

                response = create_response_obj(flight)

        return jsonify(
            {
                "message": "You created a new flight",
                "flight": response}
        ), 201

    def update(flight_id):
        """Allows admin users to update or edit flight"""

        user = get_jwt_identity()
        try:
            check_admin_user(user)
        except AssertionError as error:
            return jsonify({'error': error.args[0]}), 403
        data = request.get_json()
        flight = flight_object(data)
        try:
            cleaned_data = validate_data(**flight)
        except AssertionError as error:
            return jsonify({'error': error.args[0]}), 409

        if cleaned_data:
            exact_flight = Flight.query.filter_by(id=flight_id).first()
            if exact_flight:
                exact_flight.update_flight(cleaned_data)
                return jsonify({"message": "Flight updated"}), 200
            else:
                return jsonify({"error": "Flight not available"}), 404

    def delete(flight_id):
        """Deletes flight object,
        Only admin can perform this action"""

        user = get_jwt_identity()
        try:
            check_admin_user(user)
        except AssertionError as error:
            return jsonify({'error': error.args[0]}), 403
        flight = Flight.query.filter_by(id=flight_id).first()
        if flight:
            flight.delete()
            return jsonify({
                "message": "{} successfully deleted".format(flight.name)}), 200
        else:
            return jsonify({
                "message": "Flight with that id does not exist"}), 404

    def flights():
        """Allow users to view all flights"""
        flights = Flight.get_flights()

        all_flights = serialize_flights(flights)
        return jsonify({"flights": all_flights}), 200

    def create_seat(flight_id):
        """Allow admin users to add seat to a flight"""

        data = request.get_json()
        seat = {'number': data.get('number')}
        try:
            cleaned_data = validate_data(**seat)
        except AssertionError as error:
            return jsonify({'error': error.args[0]}), 409
        if cleaned_data:
            target_flight = Flight.query.filter_by(id=flight_id).first()
            if target_flight:
                number = cleaned_data.get('number') + target_flight.name[:2].upper()
                existing_seats = Seat.query.filter_by(number=number).all()
                for seat in existing_seats:
                    if seat.flight_id == flight_id:
                        return jsonify({
                            'error': "That seat number has been added"}), 409
                seat = Seat(number=number, flight_id=flight_id, booked=False)
                seat.save_seat()
                return jsonify({"message": "Seat added Successfully"}), 201
            else:
                return jsonify({
                    "message": "Flight with that ID does not exist"}), 404

    def update_seat(flight_id, seat_id):
        """Allow admin users to update or edit flight seat"""

        user = get_jwt_identity()
        try:
            check_admin_user(user)
        except AssertionError as error:
            return jsonify({'error': error.args[0]}), 403
        data = request.get_json()
        seat = {'number': data.get('number')}
        try:
            cleaned_data = validate_data(**seat)
        except AssertionError as error:
            return jsonify({'error': error.args[0]}), 409

        if cleaned_data:
            exact_flight = Flight.query.filter_by(id=flight_id).first()
            if exact_flight:
                exact_seat = Seat.query.filter_by(id=seat_id).first()
                if not exact_seat:
                    return jsonify({"error": "Seat not available"}), 404
                if exact_flight.id == exact_seat.flight_id:
                    number = cleaned_data.get('number') + exact_flight.name[:2].upper()
                    new_seat = {'number': number}
                    exact_seat.update_seat(new_seat)
                    return jsonify({"message": "Seat updated"}), 200
                else:
                    return jsonify({
                        "error": "Seat not assigned to this flight"}), 404
            else:
                return jsonify({"error": "Flight not available"}), 404

    def delete_seat(flight_id, seat_id):
        """Allows admin users to delete seat of a particular flight"""

        user = get_jwt_identity()
        try:
            check_admin_user(user)
        except AssertionError as error:
            return jsonify({'error': error.args[0]}), 403
        exact_flight = Flight.query.filter_by(id=flight_id).first()
        if exact_flight:
            exact_seat = Seat.query.filter_by(id=seat_id).first()
            if not exact_seat:
                return jsonify({"error": "Seat not available"}), 404
            if exact_flight.id == exact_seat.flight_id:
                exact_seat.delete()
                return jsonify({"message": "Seat deleted"}), 200
            else:
                return jsonify({
                    "error": "Seat not assigned to this flight"}), 404
        else:
            return jsonify({"error": "Flight not available"}), 404

    def seats(flight_id):
        """Returns all seats of a particular flight"""

        seats = Seat.query.all()
        flight_seats = [
            {"_id": seat.id,
                "flight_id": seat.flight_id,
                "booked": seat.booked,
                "number": seat.number} for seat in seats if seat.flight_id == flight_id]
        return jsonify({"seats": flight_seats}), 200
