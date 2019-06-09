import unittest
import json
from urllib.parse import urljoin
from flights import app, db
from config import app_config

from flights.models.user import User


class BaseTestSetUp(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app
        self.app.config.from_object(app_config['testing'])
        self.app = app.test_client()
        self.testHelper = TestHelper()
        self.base_url = self.testHelper.base_url
        self.app = self.testHelper.app
        self.headers = self.testHelper.headers

        with app.app_context():
            # create all tables
            db.session.close()
            db.drop_all()
            db.create_all()


class TestHelper():

    def __init__(self):
        self.base_url = 'http://127.0.0.1:5000'
        self.headers = {'content-type': 'application/json'}
        self.app = app.test_client()
    
    # Create a new user
    def add_user(self, user_data):
        url = self.base_url + '/api/user/register'
        result = self.app.post(url, data=json.dumps(
            user_data), headers=self.headers)
        return result
    
    def login_user(self, user_data):
        url = self.base_url + '/api/user/login'
        result = self.app.post(url, data=json.dumps(
            user_data), headers=self.headers)
        return result
    
    #logout a user
    def logout_user(self, token=None):
        url = self.base_url + '/api/user/logout'
        return self.app.post(
            url,
            headers={
                **self.headers,
                'Authorization': 'Bearer {}'.format(token)})

    def create_flight(self, new_flight, token):
        url = self.base_url + '/api/flight'
        return self.app.post(
            url,
            data=json.dumps(new_flight),
            headers={
                **self.headers,
                "Authorization": 'Bearer {}'.format(token)})

    #Retrieve all the available flights
    def get_flights(self):
        url = self.base_url + '/api/flights'
        return self.app.get(url)
    
    #method to get flight by id
    def get_flight_by_id(self, flight_id):
        url = self.base_url + '/api/flight/{id}'.format(id=flight_id)
        return self.app.get(url)

    def update_flight(self, flight_id, update_data, token):

        url = self.base_url + f'/api/flight/{light_id}'
        return self.app.put(
            url,
            data=json.dumps(update_data),
            headers={
                **self.headers,
                'authorization': 'Bearer {}'.format(token)})
    
    #method to delete flight
    def delete_flight(self, flight_id, token):
        url = self.base_url + '/api/flight/{}'.format(flight_id)
        return self.app.delete(
            url,
            headers={
                **self.headers,
                'Authorization': 'Bearer {}'.format(token)})

     # Add seat to a flight method

    def create_seat(self, flight_id, new_seat, token):
        url = urljoin(
            self.base_url, '/api/{id}/seats'.format(id=str(flight_id)))
        return self.app.post(
            url, data=json.dumps(new_seat), headers={
                **self.headers, 'Authorization': 'Bearer {}'.format(token)})

    def get_all_seats(self, flight_id):
        url = urljoin(
            self.base_url, '/api/{id}/seats'.format(id=str(flight_id)))
        return self.app.get(url)

    def book_flight(self, booking, token):
        url = self.base_url + '/api/booking'
        return self.app.post(
            url,
            data=json.dumps(booking),
            headers={
                **self.headers,
                "Authorization": 'Bearer {}'.format(token)})
    
    def get_user_bookings(self,token):
        url = self.base_url + '/api/booking'
        return self.app.get(
            url,
            headers={
                **self.headers,
                "Authorization": 'Bearer {}'.format(token)})
