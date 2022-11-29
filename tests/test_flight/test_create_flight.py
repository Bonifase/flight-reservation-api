import unittest
import json
from tests import BaseTestSetUp
from tests.test_flight.flight_data import *
from tests.test_users.data_source import *


class TestFlightCase(BaseTestSetUp):

    def test_user_can_create_flight(self):
        """Test API can create flight (POST request)"""

        self.testHelper.add_user(new_user)
        self.result = self.testHelper.login_user(new_user)
        self.token = json.loads(self.result.data.decode())['AuthToken']
        response = self.testHelper.create_flight(new_flight=new_flight,token=self.token)
        result = json.loads(response.data.decode())
        self.assertIn(result[
            "message"], "You created a new flight")
        self.assertEqual(response.status_code, 201)
    
    def test_regular_user_cannot_create_flight(self):
        """Test API cannot create flight for regular user (POST request)"""

        self.testHelper.add_user(regular_user)
        self.result = self.testHelper.login_user(regular_user)
        self.token = json.loads(self.result.data.decode())['AuthToken']
        response = self.testHelper.create_flight(new_flight=new_flight,token=self.token)
        result = json.loads(response.data.decode())
        self.assertIn(result[
            "error"], "You are not authorised to perform this action")
        self.assertEqual(response.status_code, 403)

    def test_user_cannot_create_same_flight_twice(self):
        """Test API cannot create same flight twice (POST request)"""

        self.testHelper.add_user(new_user)
        self.result = self.testHelper.login_user(new_user)
        self.token = json.loads(self.result.data.decode())['AuthToken']
        self.testHelper.create_flight(new_flight=new_flight,token=self.token)
        response = self.testHelper.create_flight(new_flight=new_flight,token=self.token)
        result = json.loads(response.data.decode())
        self.assertIn(result[
            "error"], "Flight already Exist, use another name")
        self.assertEqual(response.status_code, 409)
    
    def test_user_cannot_create_flight_with_missing_name(self):
        """Test API cannot create flight with missing name(POST request)"""

        self.testHelper.add_user(new_user)
        self.result = self.testHelper.login_user(new_user)
        self.token = json.loads(self.result.data.decode())['AuthToken']
        response = self.testHelper.create_flight(new_flight=missing_name,token=self.token)
        result = json.loads(response.data.decode())
        self.assertIn(result[
            "error"], "name is required field")
        self.assertEqual(response.status_code, 409)

    def test_user_cannot_create_flight_with_missing_departure(self):
        """Test API cannot create flight with missing departutre time (POST request)"""

        self.testHelper.add_user(new_user)
        self.result = self.testHelper.login_user(new_user)
        self.token = json.loads(self.result.data.decode())['AuthToken']
        response = self.testHelper.create_flight(new_flight=missing_departure,token=self.token)
        result = json.loads(response.data.decode())
        self.assertIn(result[
            "error"], "departure is required field")
        self.assertEqual(response.status_code, 409)

    def test_user_cannot_create_flight_with_missing_arrival(self):
        """Test API cannot create flight with missing arrival time (POST request)"""

        self.testHelper.add_user(new_user)
        self.result = self.testHelper.login_user(new_user)
        self.token = json.loads(self.result.data.decode())['AuthToken']
        response = self.testHelper.create_flight(new_flight=missing_arrival,token=self.token)
        result = json.loads(response.data.decode())
        self.assertIn(result[
            "error"], "arrival is required field")
        self.assertEqual(response.status_code, 409)

    def test_user_cannot_create_flight_with_missing_destination(self):
        """Test API cannot create flight with missing destination (POST request)"""

        self.testHelper.add_user(new_user)
        self.result = self.testHelper.login_user(new_user)
        self.token = json.loads(self.result.data.decode())['AuthToken']
        response = self.testHelper.create_flight(new_flight=missing_destination,token=self.token)
        result = json.loads(response.data.decode())
        self.assertIn(result[
            "error"], "destination is required field")
        self.assertEqual(response.status_code, 409)

    def test_user_cannot_create_flight_with_invalid_name(self):
        """Test API cannot create flight with invalid name (POST request)"""

        self.testHelper.add_user(new_user)
        self.result = self.testHelper.login_user(new_user)
        self.token = json.loads(self.result.data.decode())['AuthToken']
        response = self.testHelper.create_flight(new_flight=invalid_name,token=self.token)
        result = json.loads(response.data.decode())
        self.assertIn(result[
            "error"], "Invalid name")
        self.assertEqual(response.status_code, 409)

    def test_user_cannot_create_flight_with_invalid_destination(self):
        """Test API cannot create flight with invalid invalid destination(POST request)"""

        self.testHelper.add_user(new_user)
        self.result = self.testHelper.login_user(new_user)
        self.token = json.loads(self.result.data.decode())['AuthToken']
        response = self.testHelper.create_flight(new_flight=invalid_destination,token=self.token)
        result = json.loads(response.data.decode())
        self.assertIn(result[
            "error"], "Invalid destination")
        self.assertEqual(response.status_code, 409)

    def test_user_cannot_create_flight_with_name_key_missing(self):
        """Test API cannot create flight with missing name key(POST request)"""

        self.testHelper.add_user(new_user)
        self.result = self.testHelper.login_user(new_user)
        self.token = json.loads(self.result.data.decode())['AuthToken']
        response = self.testHelper.create_flight(new_flight=missing_name_key,token=self.token)
        result = json.loads(response.data.decode())
        self.assertIn(result[
            "error"], "name key is missing")
        self.assertEqual(response.status_code, 409)
    
    def test_user_cannot_create_flight_with_departure_key_missing(self):
        """Test API cannot create flight with missing departure key(POST request)"""

        self.testHelper.add_user(new_user)
        self.result = self.testHelper.login_user(new_user)
        self.token = json.loads(self.result.data.decode())['AuthToken']
        response = self.testHelper.create_flight(new_flight=missing_departure_key,token=self.token)
        result = json.loads(response.data.decode())
        self.assertIn(result[
            "error"], "departure key is missing")
        self.assertEqual(response.status_code, 409)
    
    def test_user_cannot_create_flight_with_arrival_key_missing(self):
        """Test API cannot create flight with missing arrival key(POST request)"""

        self.testHelper.add_user(new_user)
        self.result = self.testHelper.login_user(new_user)
        self.token = json.loads(self.result.data.decode())['AuthToken']
        response = self.testHelper.create_flight(new_flight=missing_arrival_key,token=self.token)
        result = json.loads(response.data.decode())
        self.assertIn(result[
            "error"], "arrival key is missing")
        self.assertEqual(response.status_code, 409)

    def test_user_cannot_create_flight_with_destination_key_missing(self):
        """Test API cannot create flight with missing destination key(POST request)"""

        self.testHelper.add_user(new_user)
        self.result = self.testHelper.login_user(new_user)
        self.token = json.loads(self.result.data.decode())['AuthToken']
        response = self.testHelper.create_flight(new_flight=missing_destination_key,token=self.token)
        result = json.loads(response.data.decode())
        self.assertIn(result[
            "error"], "destination key is missing")
        self.assertEqual(response.status_code, 409)

    def test_user_get_all_flights(self):
        """Test API can get all flights (GET request)"""

        self.testHelper.add_user(new_user)
        self.result = self.testHelper.login_user(new_user)
        self.token = json.loads(self.result.data.decode())['AuthToken']
        self.testHelper.create_flight(new_flight=new_flight,token=self.token)
        response = self.testHelper.get_flights()
        result = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)

    def test_user_cannot_get_empty_flights(self):
        """Test API returns an empty list when there are no flights (GET request)"""

        self.testHelper.add_user(new_user)
        self.result = self.testHelper.login_user(new_user)
        response = self.testHelper.get_flights()
        result = json.loads(response.data.decode())
        self.assertEqual(result["flights"], [])
        self.assertEqual(response.status_code, 200)
