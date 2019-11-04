from flights import app
from flask_jwt_extended import jwt_required
from flights.controller.booking_controller import BookingController


@app.route('/api/booking', methods=['POST'])
@jwt_required
def create_booking():
    """Create new booking"""
    
    return BookingController.create()
    

@app.route('/api/booking', methods=['GET'])
@jwt_required
def get_bookings():
    """Allows logged in users to see their bookings"""
    
    return BookingController.bookings()
    

@app.route('/api/bookings/<int:flight_id>', methods=['GET'])
@jwt_required
def get_flight_bookings(flight_id):
    """Get all bookings of a flight"""

    return BookingController.flight_bookings(flight_id)