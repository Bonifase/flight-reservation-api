from flights.models.user import User
from flights.models.flight import Flight,Seat

def check_admin_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if not user.isAdmin:    
        assert False, "You are not authorised to perform this action"

def get_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    return user

def get_flight(flight_id):
    flight = Flight.query.filter_by(id=flight_id).first()
    if flight is None:
        assert False, "Flight does not exist"
    else:
        return flight
def check_available_slot(user, data):
    flight = Flight.query.filter_by(
                name=data['flight_name']).first()
    if not flight:    
        assert False, "Flight with such a name does not exist"
    seats = Seat.query.filter_by(
        number=data['seat_number']).all()
    flight_seats = []
    for seat in seats:
        if seat.flight_id == flight.id: 
            flight_seats.append(seat)
    if flight_seats:
            for seat in flight_seats:
                if seat.booked:
                        assert False, "Seat has been booked"
                return flight, seat   
            
    else:
        assert False, "Seat number does not belong to this flight"
   