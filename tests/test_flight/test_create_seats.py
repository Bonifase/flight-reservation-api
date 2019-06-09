import unittest
import json
from tests import BaseTestSetUp
from tests.test_flight.flight_data import *
from tests.test_users.data_source import *


class TestFlightCase(BaseTestSetUp):

    def test_user_can_create_seat(self):
        """Test API can create seat (POST request)"""

        self.testHelper.add_user(new_user)
        self.result = self.testHelper.login_user(new_user)
        self.token = json.loads(self.result.data.decode())['AuthToken']
        self.testHelper.create_flight(new_flight=new_flight,token=self.token)
        response = self.testHelper.create_seat(
            new_seat=new_seat,
            token=self.token, 
            flight_id=1)
        result = json.loads(response.data.decode())
        self.assertIn(result[
            "message"], "Seat added Successfully")
        self.assertEqual(response.status_code, 201)
    
    def test_user_cannot_create_seat_with_same_number_twice(self):
        """Test API cannot create seat with same number twice(POST request)"""

        self.testHelper.add_user(new_user)
        self.result = self.testHelper.login_user(new_user)
        self.token = json.loads(self.result.data.decode())['AuthToken']
        self.testHelper.create_flight(new_flight=new_flight,token=self.token)
        self.testHelper.create_seat(
            new_seat=new_seat,
            token=self.token, 
            flight_id=1)
        response = self.testHelper.create_seat(
            new_seat=new_seat,
            token=self.token, 
            flight_id=1)
        result = json.loads(response.data.decode())
        self.assertIn(result[
            "error"], "That seat number has been added to this flight")
        self.assertEqual(response.status_code, 409)

    
    def test_user_cannot_create_seat_with_missing_number(self):
        """Test API cannot create seat with missing number(POST request)"""

        self.testHelper.add_user(new_user)
        self.result = self.testHelper.login_user(new_user)
        self.token = json.loads(self.result.data.decode())['AuthToken']
        self.testHelper.create_flight(new_flight=new_flight,token=self.token)
        response = self.testHelper.create_seat(
            new_seat=missing_number,
            token=self.token, 
            flight_id=1)
        result = json.loads(response.data.decode())
        self.assertIn(result[
            "error"], "number is required field")
        self.assertEqual(response.status_code, 409)

    def test_user_cannot_create_seat_for_unavailable_flight(self):
        """Test API cannot create seat for unavailable flight(POST request)"""

        self.testHelper.add_user(new_user)
        self.result = self.testHelper.login_user(new_user)
        self.token = json.loads(self.result.data.decode())['AuthToken']
        response = self.testHelper.create_seat(
            new_seat=new_seat,
            token=self.token, 
            flight_id=1)
        result = json.loads(response.data.decode())
        self.assertIn(result[
            "message"], "Flight with that ID does not exist")
        self.assertEqual(response.status_code, 404)

    def test_user_cannot_create_seat_with_missing_number_key(self):
        """Test API cannot create seat with missing number key(POST request)"""

        self.testHelper.add_user(new_user)
        self.result = self.testHelper.login_user(new_user)
        self.token = json.loads(self.result.data.decode())['AuthToken']
        self.testHelper.create_flight(new_flight=new_flight,token=self.token)
        response = self.testHelper.create_seat(
            new_seat=number_key_missing,
            token=self.token, 
            flight_id=1)
        result = json.loads(response.data.decode())
        self.assertIn(result[
            "error"], "number key is missing")
        self.assertEqual(response.status_code, 409)

    def test_user_can_get_all_seats(self):
        """Test API can get all seats(GET request)"""

        self.testHelper.add_user(new_user)
        self.result = self.testHelper.login_user(new_user)
        self.token = json.loads(self.result.data.decode())['AuthToken']
        self.testHelper.create_flight(new_flight=new_flight,token=self.token)
        self.testHelper.create_seat(
            new_seat=number_key_missing,
            token=self.token, 
            flight_id=1)   
        response = self.testHelper.get_all_seats( 
            flight_id=1)
        result = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
    
    def test_user_get_empty_list_no_seats(self):
        """Test API returns an empty list if there is no seats(GET request)"""

        self.testHelper.add_user(new_user)
        self.result = self.testHelper.login_user(new_user)
        self.token = json.loads(self.result.data.decode())['AuthToken']
        self.testHelper.create_flight(new_flight=new_flight,token=self.token)
        response = self.testHelper.get_all_seats( 
            flight_id=1)
        result = json.loads(response.data.decode())
        self.assertEqual(result["seats"], [])
        self.assertEqual(response.status_code, 200)
    