import unittest
import json
from tests import BaseTestSetUp
from tests.test_flight.flight_data import *
from tests.test_users.data_source import *


class TestFlightCase(BaseTestSetUp):

    def test_user_can_delete_flight(self):
        """Test API can delete flight (DELETE request)"""

        self.testHelper.add_user(new_user)
        self.result = self.testHelper.login_user(new_user)
        self.token = json.loads(self.result.data.decode())['AuthToken']
        self.testHelper.create_flight(new_flight=new_flight,token=self.token)
        response = self.testHelper.delete_flight(flight_id=1,token=self.token)
        result = json.loads(response.data.decode())
        self.assertIn(result[
            "message"], "Flight No 3 successfully deleted")
        self.assertEqual(response.status_code, 200)

    def test_user_cannot_delete_non_existant_flight(self):
        """Test API can delete flight (DELETE request)"""

        self.testHelper.add_user(new_user)
        self.result = self.testHelper.login_user(new_user)
        self.token = json.loads(self.result.data.decode())['AuthToken']
        self.testHelper.create_flight(new_flight=new_flight,token=self.token)
        response = self.testHelper.delete_flight(flight_id=4,token=self.token)
        result = json.loads(response.data.decode())
        self.assertIn(result[
            "message"], "Flight with that id does not exist")
        self.assertEqual(response.status_code, 404)
    
    def test_regular_user_cannot_delete_flight(self):
        """Test API cannot delete flight for regular user (DELETE request)"""

        self.testHelper.add_user(new_user)
        self.testHelper.add_user(regular_user)
        self.result = self.testHelper.login_user(new_user)
        self.token = json.loads(self.result.data.decode())['AuthToken']
        self.testHelper.create_flight(new_flight=new_flight,token=self.token)
        self.result = self.testHelper.login_user(regular_user)
        self.token = json.loads(self.result.data.decode())['AuthToken']
        response = self.testHelper.delete_flight(flight_id=4,token=self.token)
        result = json.loads(response.data.decode())
        self.assertIn(result[
            "error"], "You are not authorised to perform this action")
        self.assertEqual(response.status_code, 403)
    
    def test_user_can_update_flight(self):
        """Test API can update flight (PUT request)"""

        self.testHelper.add_user(new_user)
        self.result = self.testHelper.login_user(new_user)
        self.token = json.loads(self.result.data.decode())['AuthToken']
        self.testHelper.create_flight(new_flight=new_flight,token=self.token)
        response = self.testHelper.update_flight(flight_id=1, update_data=update_flight,token=self.token)
        print(response)
        result = json.loads(response.data.decode())
        self.assertIn(result[
            "message"], "Flight updated")
        self.assertEqual(response.status_code, 200)
    
    def test_user_cannot_update_non_existant_flight(self):
        """Test API cannot update non existant flight (PUT request)"""

        self.testHelper.add_user(new_user)
        self.result = self.testHelper.login_user(new_user)
        self.token = json.loads(self.result.data.decode())['AuthToken']
        self.testHelper.create_flight(new_flight=new_flight,token=self.token)
        response = self.testHelper.update_flight(flight_id=3, update_data=update_flight,token=self.token)
        result = json.loads(response.data.decode())
        self.assertIn(result[
            "error"], "Flight not available")
        self.assertEqual(response.status_code, 404)

    def test_regular_user_cannot_update_flight(self):
        """Test API cannot update flight for non admin user (PUT request)"""

        self.testHelper.add_user(new_user)
        self.testHelper.add_user(regular_user)
        self.result = self.testHelper.login_user(new_user)
        self.token = json.loads(self.result.data.decode())['AuthToken']
        self.testHelper.create_flight(new_flight=new_flight,token=self.token)
        self.result = self.testHelper.login_user(regular_user)
        self.token = json.loads(self.result.data.decode())['AuthToken']
        response = self.testHelper.update_flight(flight_id=1, update_data=update_flight, token=self.token)
        result = json.loads(response.data.decode())
        self.assertIn(result[
            "error"], "You are not authorised to perform this action")
        self.assertEqual(response.status_code, 403)

    def test_user_cannot_update_flight_with_missing_name(self):
        """Test API cannot update flight with missing name(PUT request)"""

        self.testHelper.add_user(new_user)
        self.result = self.testHelper.login_user(new_user)
        self.token = json.loads(self.result.data.decode())['AuthToken']
        response = self.testHelper.create_flight(new_flight=missing_name,token=self.token)
        result = json.loads(response.data.decode())
        self.assertIn(result[
            "error"], "name is required field")
        self.assertEqual(response.status_code, 409)

    def test_user_cannot_update_flight_with_missing_departure(self):
        """Test API cannot update flight with missing departutre time (PUT request)"""

        self.testHelper.add_user(new_user)
        self.result = self.testHelper.login_user(new_user)
        self.token = json.loads(self.result.data.decode())['AuthToken']
        response = self.testHelper.create_flight(new_flight=missing_departure,token=self.token)
        result = json.loads(response.data.decode())
        self.assertIn(result[
            "error"], "departure is required field")
        self.assertEqual(response.status_code, 409)

    def test_user_cannot_uppdate_flight_with_missing_arrival(self):
        """Test API cannot create flight with missing arrival time (PUT request)"""

        self.testHelper.add_user(new_user)
        self.result = self.testHelper.login_user(new_user)
        self.token = json.loads(self.result.data.decode())['AuthToken']
        response = self.testHelper.create_flight(new_flight=missing_arrival,token=self.token)
        result = json.loads(response.data.decode())
        self.assertIn(result[
            "error"], "arrival is required field")
        self.assertEqual(response.status_code, 409)

    def test_user_cannot_update_flight_with_missing_destination(self):
        """Test API cannot create flight with missing destination (PUT request)"""

        self.testHelper.add_user(new_user)
        self.result = self.testHelper.login_user(new_user)
        self.token = json.loads(self.result.data.decode())['AuthToken']
        response = self.testHelper.create_flight(new_flight=missing_destination,token=self.token)
        result = json.loads(response.data.decode())
        self.assertIn(result[
            "error"], "destination is required field")
        self.assertEqual(response.status_code, 409)

    def test_user_cannot_update_flight_with_invalid_name(self):
        """Test API cannot update flight with invalid name (PUT request)"""

        self.testHelper.add_user(new_user)
        self.result = self.testHelper.login_user(new_user)
        self.token = json.loads(self.result.data.decode())['AuthToken']
        response = self.testHelper.create_flight(new_flight=invalid_name,token=self.token)
        result = json.loads(response.data.decode())
        self.assertIn(result[
            "error"], "Invalid name")
        self.assertEqual(response.status_code, 409)

    def test_user_cannot_update_flight_with_invalid_destination(self):
        """Test API cannot update flight with invalid destination(PUT request)"""

        self.testHelper.add_user(new_user)
        self.result = self.testHelper.login_user(new_user)
        self.token = json.loads(self.result.data.decode())['AuthToken']
        response = self.testHelper.create_flight(new_flight=invalid_destination,token=self.token)
        result = json.loads(response.data.decode())
        self.assertIn(result[
            "error"], "Invalid destination")
        self.assertEqual(response.status_code, 409)

    def test_user_cannot_update_flight_with_name_key_missing(self):
        """Test API cannot update flight with missing name key(PUT request)"""

        self.testHelper.add_user(new_user)
        self.result = self.testHelper.login_user(new_user)
        self.token = json.loads(self.result.data.decode())['AuthToken']
        response = self.testHelper.create_flight(new_flight=missing_name_key,token=self.token)
        result = json.loads(response.data.decode())
        self.assertIn(result[
            "error"], "name key is missing")
        self.assertEqual(response.status_code, 409)
    
    def test_user_cannot_update_flight_with_departure_key_missing(self):
        """Test API cannot update flight with missing departure key(PUT request)"""

        self.testHelper.add_user(new_user)
        self.result = self.testHelper.login_user(new_user)
        self.token = json.loads(self.result.data.decode())['AuthToken']
        response = self.testHelper.create_flight(new_flight=missing_departure_key,token=self.token)
        result = json.loads(response.data.decode())
        self.assertIn(result[
            "error"], "departure key is missing")
        self.assertEqual(response.status_code, 409)
    
    def test_user_cannot_update_flight_with_arrival_key_missing(self):
        """Test API cannot update flight with missing arrival key(PUT request)"""

        self.testHelper.add_user(new_user)
        self.result = self.testHelper.login_user(new_user)
        self.token = json.loads(self.result.data.decode())['AuthToken']
        response = self.testHelper.create_flight(new_flight=missing_arrival_key,token=self.token)
        result = json.loads(response.data.decode())
        self.assertIn(result[
            "error"], "arrival key is missing")
        self.assertEqual(response.status_code, 409)

    def test_user_cannot_update_flight_with_destination_key_missing(self):
        """Test API cannot update flight with missing destination key(PUT request)"""

        self.testHelper.add_user(new_user)
        self.result = self.testHelper.login_user(new_user)
        self.token = json.loads(self.result.data.decode())['AuthToken']
        response = self.testHelper.create_flight(new_flight=missing_destination_key,token=self.token)
        result = json.loads(response.data.decode())
        self.assertIn(result[
            "error"], "destination key is missing")
        self.assertEqual(response.status_code, 409)