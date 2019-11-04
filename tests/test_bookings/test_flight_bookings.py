import unittest
import json
from tests import BaseTestSetUp
from tests.test_flight.flight_data import *
from tests.test_users.data_source import *
from tests.test_bookings.bookings_data import *


class TestBookingCase(BaseTestSetUp):

    def test_user_can_get_all_bookings_of_flight(self):
        """Test API get all bookings of a flight (GET request)"""

        self.testHelper.add_user(new_user)
        self.result = self.testHelper.login_user(new_user)
        self.token = json.loads(self.result.data.decode())['AuthToken']
        self.testHelper.create_flight(new_flight=new_flight,token=self.token)
        self.testHelper.create_seat(
            new_seat=new_seat,
            token=self.token, 
            flight_id=1)
        self.testHelper.book_flight(
            booking=new_booking,token=self.token)
        response = self.testHelper.get_flight_bookings(token=self.token, flight_id=1)
        result = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)

    def test_user_get_empty_list_when_no_bookings_found(self):
        """Test API returns empty list when no flight bookings found (GET request)"""

        self.testHelper.add_user(new_user)
        self.result = self.testHelper.login_user(new_user)
        self.token = json.loads(self.result.data.decode())['AuthToken']
        self.testHelper.create_flight(new_flight=new_flight,token=self.token)
        self.testHelper.create_seat(
            new_seat=new_seat,
            token=self.token, 
            flight_id=1)
        response = self.testHelper.get_flight_bookings(token=self.token, flight_id=1)
        result = json.loads(response.data.decode())
        self.assertEqual(result[
            "flight_bookings"], [])
        self.assertEqual(response.status_code, 200)
    
    def test_user_cannot_bookings_for_unavailable_flight(self):
        """Test API cannot get flight bookings for unavailable flight (GET request)"""

        self.testHelper.add_user(new_user)
        self.result = self.testHelper.login_user(new_user)
        self.token = json.loads(self.result.data.decode())['AuthToken']
        self.testHelper.create_flight(new_flight=new_flight,token=self.token)
        self.testHelper.create_seat(
            new_seat=new_seat,
            token=self.token, 
            flight_id=1)
        response = self.testHelper.get_flight_bookings(token=self.token, flight_id=2)
        result = json.loads(response.data.decode())
        self.assertEqual(result[
            "error"], "Flight does not exist")
        self.assertEqual(response.status_code, 404)