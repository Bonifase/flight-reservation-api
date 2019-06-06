
from flights import db, app
from flask_bcrypt import Bcrypt
from sqlalchemy.ext.hybrid import hybrid_property
from flights.models.validate_fields import *

class Flight(db.Model):
    """This class defines the flight table."""

    __tablename__ = 'flights'

    id = db.Column(db.Integer, primary_key=True)
    _name = db.Column("name", db.String(80), unique=True)
    _departure = db.Column("departure", db.DateTime)
    _arrival = db.Column("arrival", db.DateTime)
    _destination = db.Column("destination", db.String(80))
    seats = db.relationship('Seat', backref='seatowner', lazy='dynamic')
    
    def __init__(self, name, departure, arrival, destination):
        self.name = name
        self.departure = departure
        self.arrival = arrival
        self.destination  = destination 

    """method that saves the flight to the database"""
    def save_flight(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_flights():
        flights = Flight.query.all()
        return flights

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @hybrid_property
    def name(self):
        return self._name

    """sets the name of the flight attribute"""
    @name.setter
    def name(self, value):       
        match = name_pattern(value)
        if match:
            self._name = value
            return
        assert 0, 'Invalid name'

    @hybrid_property
    def departure(self):
        return self._departure

    @departure.setter
    def departure(self, value):       
        match = True
        if match:
            self._departure = value
            return
        assert 0, 'Invalid times'

    @hybrid_property
    def arrival(self):
        return self._arrival

    @arrival.setter
    def arrival(self, value):      
        match = True
        if match:
            self._arrival = value
            return
        assert 0, 'Invalid time'

    @hybrid_property
    def destination(self):
        return self._destination

    """sets the destination of the flight attribute"""
    @destination.setter
    def destination(self, value):       
        match = name_pattern(value)
        if match:
            self._destination = value
            return
        assert 0, 'Invalid destination'


class Seat(db.Model):
    """This class defines the seat table."""

    __tablename__ = 'seats'

    id = db.Column(db.Integer, primary_key=True)
    _number = db.Column("number", db.String(80))
    booked = db.Column("booked", db.Boolean(), default=False)
    flight_id = db.Column(db.Integer, db.ForeignKey('flights.id', ondelete="CASCADE", onupdate="CASCADE"))

    def __init__(self, number, flight_id, booked):
        self._number = number
        self.booked = False
        self.flight_id = flight_id

    @staticmethod
    def seats():
        seats = Seat.query.all()
        return seats

    def save_seat(self):
        db.session.add(self)
        db.session.commit()

    def book_seat(self):
        Seat.booked = True
        db.session.add(self)
        db.session.commit()


    @hybrid_property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):      
        match = number_pattern(value)
        if match:
            self._number = value
            return
        assert 0, 'Invalid number'  