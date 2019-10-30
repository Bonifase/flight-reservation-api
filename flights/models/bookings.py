from flights import db, app
from sqlalchemy.ext.hybrid import hybrid_property


class Booking(db.Model):
    """This class defines the booked flight table."""

    __tablename__ = 'bookings'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column("user_id", db.Integer())
    flight_name = db.Column("flight_name", db.String(80))
    seat_number = db.Column("seat_number", db.String(80))
    payment = db.Column("payment", db.String(80))
    date_booked = db.Column("date_booked", db.DateTime)

    """method that saves the flight to the database"""
    def save_booking(self):
        db.session.add(self)
        db.session.commit()

    def __str__(self):

        return self.flight_name
