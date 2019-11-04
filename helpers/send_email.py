import os
from flask_mail import Message, Mail
from flights import app
from flights.models.bookings import Booking
from flights.models.flight import Flight
from flights.models.user import User
import datetime
import time

mail = Mail(app)
sender = os.getenv('MAIL_USERNAME')
def send_email(loop_on):
   while True:
      if loop_on.value == True:
              with app.app_context():
                bookings = Booking.query.all()
                date = datetime.datetime.now()
                if bookings:
                        # print("I love coding",bookings)
                        for booking in bookings:
                                flights = Flight.query.filter_by(name=booking.flight_name).all()
                                for flight in flights:
                                        if flight.departure < datetime.datetime.now():
                                                users = User.query.filter_by(id=booking.user_id).all()
                                                for user in users:
                                                        message = 'Your light is leaving in 24 hours time'
                                                        subject = "hello, {}".format(user.username)
                                                        msg = Message(body=message,
                                                        sender=sender,recipients=[user.email],subject=subject)

                                                        mail.send(msg)
                                        time.sleep(10)


