
def create_object(self, db):
    """Create new item in the database"""

    db.session.add(self)
    db.session.commit()


def create_response_obj(booking=None, flight=None, user=None):
    """Create a json serializable object"""

    if flight and booking is None:
        obj = dict(
            _id=flight.id,
            Name=flight.name,
            Departure=flight.departure,
            arrival=flight.arrival,
            destination=flight.destination
        )

    elif flight and booking:
        obj = dict(
            _id=booking.id,
            flight=booking.flight_name,
            seat=booking.seat_number,
            payment=booking.payment,
            date_booked=booking.date_booked,
            departure=flight.departure,
            destination=flight.destination,
        )
        if user:
            obj['user'] = user

        return obj


def query_flight_objects(bookings=None, flights=None, user=None):
    """Returns bookings made by user"""

    user_bookings = [
        {
            '_id': booking.id,
            'flight': booking.flight_name,
            'seat': booking.seat_number,
            'payment': booking.payment,
            'date_booked': booking.date_booked,
            'user_id': user} for booking in bookings if booking.user_id == user]  # noqa
    return user_bookings


def get_flight_bookings(bookings, flight, user):
    """Get all bookings of a flight"""

    flight_bookings = [
            {
                '_id': booking.id,
                'flight': booking.flight_name,
                'seat': booking.seat_number,
                'payment': booking.payment,
                'departure': flight.departure,
                'arrival': flight.arrival,
                'destination': flight.destination,
                'user': user.username} for booking in bookings if booking.flight_name == flight.name]  # noqa

    return flight_bookings


def flight_object(data):
    """creates flight object"""

    flight = dict(
        name=data.get('name'),
        departure=data.get('departure'),
        arrival=data.get('arrival'),
        destination=data.get('destination')
    )
    return flight


def serialize_flights(flights):
    """Returns serialized flight data"""

    flights = [{
        '_id': flight.id,
        'Name': flight.name,
        'Departure': "{:%Y-%m-%d %H:%M}".format(flight.departure),
        'arrival': "{:%Y-%m-%d %H:%M}".format(flight.arrival),
        'destination': flight.destination} for flight in flights]
    return flights
