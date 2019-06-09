import unittest
import json
from tests import BaseTestSetUp
from tests.test_flight.flight_data import *
from tests.test_users.data_source import *
from tests.test_bookings.bookings_data import *


class TestFlightCase(BaseTestSetUp):

    def test_user_can_book_flight(self):
        """Test API can book flight (POST request)"""

        self.testHelper.add_user(new_user)
        self.result = self.testHelper.login_user(new_user)
        self.token = json.loads(self.result.data.decode())['AuthToken']
        self.testHelper.create_flight(new_flight=new_flight,token=self.token)
        self.testHelper.create_seat(
            new_seat=new_seat,
            token=self.token, 
            flight_id=1)
        response = self.testHelper.book_flight(booking=new_booking,token=self.token)
        result = json.loads(response.data.decode())
        self.assertIn(result[
            "message"], "You Booked sucessfully")
        self.assertEqual(response.status_code, 201)
    
    def test_user_cannot_book_same_seat_twice(self):
        """Test API cannot book already booked seat (POST request)"""

        self.testHelper.add_user(new_user)
        self.result = self.testHelper.login_user(new_user)
        self.token = json.loads(self.result.data.decode())['AuthToken']
        self.testHelper.create_flight(new_flight=new_flight,token=self.token)
        self.testHelper.create_seat(
            new_seat=new_seat,
            token=self.token, 
            flight_id=1)
        self.testHelper.book_flight(booking=new_booking,token=self.token)
        response = self.testHelper.book_flight(booking=new_booking,token=self.token)
        result = json.loads(response.data.decode())
        self.assertIn(result[
            "error"], "Seat has been booked")
        self.assertEqual(response.status_code, 409)
    
    def test_user_cannot_book_with_blank_flight(self):
        """Test API cannot book with blank flight name (POST request)"""

        self.testHelper.add_user(new_user)
        self.result = self.testHelper.login_user(new_user)
        self.token = json.loads(self.result.data.decode())['AuthToken']
        self.testHelper.create_flight(new_flight=new_flight,token=self.token)
        self.testHelper.create_seat(
            new_seat=new_seat,
            token=self.token, 
            flight_id=1)
        response = self.testHelper.book_flight(
            booking=blank_flight,token=self.token)
        result = json.loads(response.data.decode())
        self.assertIn(result[
            "error"], "flight_name is required field")
        self.assertEqual(response.status_code, 409)

    def test_user_cannot_book_with_blank_seat(self):
        """Test API cannot book with blank seat number (POST request)"""

        self.testHelper.add_user(new_user)
        self.result = self.testHelper.login_user(new_user)
        self.token = json.loads(self.result.data.decode())['AuthToken']
        self.testHelper.create_flight(new_flight=new_flight,token=self.token)
        self.testHelper.create_seat(
            new_seat=new_seat,
            token=self.token, 
            flight_id=1)
        response = self.testHelper.book_flight(
            booking=blank_seat,token=self.token)
        result = json.loads(response.data.decode())
        self.assertIn(result[
            "error"], "seat_number is required field")
        self.assertEqual(response.status_code, 409)
    
    def test_user_cannot_book_without_payment(self):
        """Test API cannot book without payment (POST request)"""

        self.testHelper.add_user(new_user)
        self.result = self.testHelper.login_user(new_user)
        self.token = json.loads(self.result.data.decode())['AuthToken']
        self.testHelper.create_flight(new_flight=new_flight,token=self.token)
        self.testHelper.create_seat(
            new_seat=new_seat,
            token=self.token, 
            flight_id=1)
        response = self.testHelper.book_flight(
            booking=no_payment,token=self.token)
        result = json.loads(response.data.decode())
        self.assertIn(result[
            "error"], "payment is required field")
        self.assertEqual(response.status_code, 409)

    def test_user_cannot_book_with_blank_flight_key(self):
        """Test API cannot book with blank flight name key (POST request)"""

        self.testHelper.add_user(new_user)
        self.result = self.testHelper.login_user(new_user)
        self.token = json.loads(self.result.data.decode())['AuthToken']
        self.testHelper.create_flight(new_flight=new_flight,token=self.token)
        self.testHelper.create_seat(
            new_seat=new_seat,
            token=self.token, 
            flight_id=1)
        response = self.testHelper.book_flight(
            booking=blank_flight_key,token=self.token)
        result = json.loads(response.data.decode())
        self.assertIn(result[
            "error"], "flight_name key is missing")
        self.assertEqual(response.status_code, 409)

    def test_user_cannot_book_with_blank_seat_key(self):
        """Test API cannot book with blank seat number key (POST request)"""

        self.testHelper.add_user(new_user)
        self.result = self.testHelper.login_user(new_user)
        self.token = json.loads(self.result.data.decode())['AuthToken']
        self.testHelper.create_flight(new_flight=new_flight,token=self.token)
        self.testHelper.create_seat(
            new_seat=new_seat,
            token=self.token, 
            flight_id=1)
        response = self.testHelper.book_flight(
            booking=blank_seat_key,token=self.token)
        result = json.loads(response.data.decode())
        self.assertIn(result[
            "error"], "seat_number key is missing")
        self.assertEqual(response.status_code, 409)
    
    def test_user_cannot_book_without_payment_key(self):
        """Test API cannot book with blank payment key (POST request)"""

        self.testHelper.add_user(new_user)
        self.result = self.testHelper.login_user(new_user)
        self.token = json.loads(self.result.data.decode())['AuthToken']
        self.testHelper.create_flight(new_flight=new_flight,token=self.token)
        self.testHelper.create_seat(
            new_seat=new_seat,
            token=self.token, 
            flight_id=1)
        response = self.testHelper.book_flight(
            booking=blank_payment_key,token=self.token)
        result = json.loads(response.data.decode())
        self.assertIn(result[
            "error"], "payment key is missing")
        self.assertEqual(response.status_code, 409)
    
    def test_user_cannot_book_non_existant_flight(self):
        """Test API cannot book non existant flight (POST request)"""

        self.testHelper.add_user(new_user)
        self.result = self.testHelper.login_user(new_user)
        self.token = json.loads(self.result.data.decode())['AuthToken']
        self.testHelper.create_seat(
            new_seat=new_seat,
            token=self.token, 
            flight_id=1)
        response = self.testHelper.book_flight(
            booking=new_booking,token=self.token)
        result = json.loads(response.data.decode())
        self.assertIn(result[
            "error"], "Flight with such a name does not exist")
        self.assertEqual(response.status_code, 409)
    
    def test_user_cannot_book_non_existant_seat(self):
        """Test API cannot book non existant seat (POST request)"""

        self.testHelper.add_user(new_user)
        self.result = self.testHelper.login_user(new_user)
        self.token = json.loads(self.result.data.decode())['AuthToken']
        self.testHelper.create_flight(new_flight=new_flight,token=self.token)
        response = self.testHelper.book_flight(
            booking=new_booking,token=self.token)
        result = json.loads(response.data.decode())
        self.assertIn(result[
            "error"], "Seat number does not exist")
        self.assertEqual(response.status_code, 409)
    
    def test_user_cannot_book_different_flight_seat(self):
        """Test API cannot book seat of different flight (POST request)"""

        self.testHelper.add_user(new_user)
        self.result = self.testHelper.login_user(new_user)
        self.token = json.loads(self.result.data.decode())['AuthToken']
        self.testHelper.create_flight(new_flight=new_flight,token=self.token)
        self.testHelper.create_flight(new_flight=another_flight,token=self.token)
        self.testHelper.create_seat(
            new_seat=new_seat,
            token=self.token, 
            flight_id=1)
        self.testHelper.create_seat(
            new_seat=new_seat,
            token=self.token, 
            flight_id=2)
        response = self.testHelper.book_flight(
            booking=another_booking,token=self.token)
        result = json.loads(response.data.decode())
        self.assertIn(result[
            "error"], "Seat number does not belong to this flight")
        self.assertEqual(response.status_code, 409)

    def test_user_can_get_all_bookings(self):
        """Test API get all bookings (POST request)"""

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
        response = self.testHelper.get_user_bookings(token=self.token)
        result = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)

    def test_user_get_empty_list_when_no_bookings_found(self):
        """Test API returns empty list when no bookings found (POST request)"""

        self.testHelper.add_user(new_user)
        self.result = self.testHelper.login_user(new_user)
        self.token = json.loads(self.result.data.decode())['AuthToken']
        self.testHelper.create_flight(new_flight=new_flight,token=self.token)
        self.testHelper.create_seat(
            new_seat=new_seat,
            token=self.token, 
            flight_id=1)
        response = self.testHelper.get_user_bookings(token=self.token)
        result = json.loads(response.data.decode())
        self.assertEqual(result[
            "bookings"], [])
        self.assertEqual(response.status_code, 200)