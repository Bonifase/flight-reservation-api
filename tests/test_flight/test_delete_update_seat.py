import unittest
import json
from tests import BaseTestSetUp
from tests.test_flight.flight_data import *
from tests.test_users.data_source import *


class TestFlightCase(BaseTestSetUp):

    def test_user_can_update_seat(self):
        """Test API can update seat (PUT request)"""

        self.testHelper.add_user(new_user)
        self.result = self.testHelper.login_user(new_user)
        self.token = json.loads(self.result.data.decode())['AuthToken']
        self.testHelper.create_flight(new_flight=new_flight,token=self.token)
        self.testHelper.create_seat(
            new_seat=new_seat,
            token=self.token, 
            flight_id=1)
        response = self.testHelper.update_seat(
            flight_id=1,
            seat_id=1,
            new_seat=update_seat,
            token=self.token 
            )
        result = json.loads(response.data.decode())
        self.assertIn(result[
            "message"], "Seat updated Successfully")
        self.assertEqual(response.status_code, 200)
    
    def test_regular_user_cannot_update_seat(self):
        """Test API cannot update seat for non admin user(PUT request)"""

        self.testHelper.add_user(regular_user)
        self.result = self.testHelper.login_user(regular_user)
        self.token = json.loads(self.result.data.decode())['AuthToken']
        self.testHelper.create_flight(new_flight=new_flight,token=self.token)
        self.testHelper.create_seat(
            new_seat=new_seat,
            token=self.token, 
            flight_id=1)
        response = self.testHelper.update_seat(
            flight_id=1,
            seat_id=1,
            new_seat=update_seat,
            token=self.token 
            )
        result = json.loads(response.data.decode())
        self.assertIn(result[
            "error"], "You are not authorised to perform this action")
        self.assertEqual(response.status_code, 403)

    
    def test_user_cannot_update_seat_with_missing_number(self):
        """Test API cannot update seat with missing number(PUT request)"""

        self.testHelper.add_user(new_user)
        self.result = self.testHelper.login_user(new_user)
        self.token = json.loads(self.result.data.decode())['AuthToken']
        self.testHelper.create_flight(new_flight=new_flight,token=self.token)
        self.testHelper.create_seat(
            new_seat=new_seat,
            token=self.token, 
            flight_id=1)
        response = self.testHelper.update_seat(
            flight_id=1,
            seat_id=1,
            new_seat=missing_number,
            token=self.token 
            )
        result = json.loads(response.data.decode())
        self.assertIn(result[
            "error"], "number is required field")
        self.assertEqual(response.status_code, 409)

    def test_user_cannot_update_seat_for_unavailable_flight(self):
        """Test API cannot update seat for unavailable flight(PUT request)"""

        self.testHelper.add_user(new_user)
        self.result = self.testHelper.login_user(new_user)
        self.token = json.loads(self.result.data.decode())['AuthToken']
        response = self.testHelper.update_seat(
            flight_id=1,
            seat_id=1,
            new_seat=update_seat,
            token=self.token 
            )
        result = json.loads(response.data.decode())
        self.assertIn(result[
            "error"], "Flight not available")
        self.assertEqual(response.status_code, 404)

    def test_user_cannot_update_unavailable_seat(self):
        """Test API cannot update unavailable seat (PUT request)"""

        self.testHelper.add_user(new_user)
        self.result = self.testHelper.login_user(new_user)
        self.token = json.loads(self.result.data.decode())['AuthToken']
        self.testHelper.create_flight(new_flight=new_flight,token=self.token)
        response = self.testHelper.update_seat(
            flight_id=1,
            seat_id=1,
            new_seat=update_seat,
            token=self.token 
            )
        result = json.loads(response.data.decode())
        self.assertIn(result[
            "error"], "Seat not available")
        self.assertEqual(response.status_code, 404)
    
    def test_user_cannot_update_seat_of_different_flight(self):
        """Test API cannot update seat for a different flight(PUT request)"""

        self.testHelper.add_user(new_user)
        self.result = self.testHelper.login_user(new_user)
        self.token = json.loads(self.result.data.decode())['AuthToken']
        self.testHelper.create_flight(new_flight=new_flight,token=self.token)
        self.testHelper.create_flight(new_flight=another_flight,token=self.token)
        self.testHelper.create_seat(
            new_seat=new_seat,
            token=self.token, 
            flight_id=1)   
        response = self.testHelper.update_seat( 
            flight_id=2, seat_id=1, new_seat=update_seat, token=self.token)
        result = json.loads(response.data.decode())
        self.assertIn(result[
            "error"], "Seat not assigned to this flight")
        self.assertEqual(response.status_code, 404)

    def test_user_can_delete_seat(self):
        """Test API can delete seat(DELETE request)"""

        self.testHelper.add_user(new_user)
        self.result = self.testHelper.login_user(new_user)
        self.token = json.loads(self.result.data.decode())['AuthToken']
        self.testHelper.create_flight(new_flight=new_flight,token=self.token)
        self.testHelper.create_seat(
            new_seat=new_seat,
            token=self.token, 
            flight_id=1)   
        response = self.testHelper.delete_seat( 
            flight_id=1, seat_id=1, token=self.token)
        result = json.loads(response.data.decode())
        self.assertIn(result[
            "message"], "Seat deleted")
        self.assertEqual(response.status_code, 200)
    
    def test_regular_user_cannot_delete_seat(self):
        """Test API cannot delete seat for non admin(DELETE request)"""

        self.testHelper.add_user(regular_user)
        self.result = self.testHelper.login_user(regular_user)
        self.token = json.loads(self.result.data.decode())['AuthToken']
        self.testHelper.create_flight(new_flight=new_flight,token=self.token)
        self.testHelper.create_seat(
            new_seat=new_seat,
            token=self.token, 
            flight_id=1)   
        response = self.testHelper.delete_seat( 
            flight_id=1, seat_id=1, token=self.token)
        result = json.loads(response.data.decode())
        self.assertIn(result[
            "error"], "You are not authorised to perform this action")
        self.assertEqual(response.status_code, 403)

    def test__user_cannot_delete_seat_for_unavalilable_seat(self):
        """Test API cannot delete seat for nonexistant seat(DELETE request)"""

        self.testHelper.add_user(new_user)
        self.result = self.testHelper.login_user(new_user)
        self.token = json.loads(self.result.data.decode())['AuthToken']  
        response = self.testHelper.delete_seat( 
            flight_id=1, seat_id=1, token=self.token)
        result = json.loads(response.data.decode())
        self.assertIn(result[
            "error"], "Flight not available")
        self.assertEqual(response.status_code, 404)

    def test_user_cannot_delete_unavailable_seat(self):
        """Test API cannot delete unavailable seat(DELETE request)"""

        self.testHelper.add_user(new_user)
        self.result = self.testHelper.login_user(new_user)
        self.token = json.loads(self.result.data.decode())['AuthToken']
        self.testHelper.create_flight(new_flight=new_flight,token=self.token)
        self.testHelper.create_seat(
            new_seat=new_seat,
            token=self.token, 
            flight_id=1)   
        response = self.testHelper.delete_seat( 
            flight_id=1, seat_id=4, token=self.token)
        result = json.loads(response.data.decode())
        self.assertIn(result[
            "error"], "Seat not available")
        self.assertEqual(response.status_code, 404)

    def test_user_cannot_delete_seat_of_different_flight(self):
        """Test API cannot delete seat for a different flight(DELETE request)"""

        self.testHelper.add_user(new_user)
        self.result = self.testHelper.login_user(new_user)
        self.token = json.loads(self.result.data.decode())['AuthToken']
        self.testHelper.create_flight(new_flight=new_flight,token=self.token)
        self.testHelper.create_flight(new_flight=another_flight,token=self.token)
        self.testHelper.create_seat(
            new_seat=new_seat,
            token=self.token, 
            flight_id=2)   
        response = self.testHelper.delete_seat( 
            flight_id=1, seat_id=1, token=self.token)
        result = json.loads(response.data.decode())
        self.assertIn(result[
            "error"], "Seat not assigned to this flight")
        self.assertEqual(response.status_code, 404)
