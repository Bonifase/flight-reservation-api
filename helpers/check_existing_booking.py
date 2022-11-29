
def check_available_slot(user, data, flight, seat):
    if not flight:    
        assert False, "Flight with such a name does not exist"
    if not seat:    
        assert False, "Seat number does not exist"
    if seat.booked:    
        assert False, "Seat has been booked"
    if seat.flight_id != flight.id:
        assert False,"Seat number does not belong to this flight"
   