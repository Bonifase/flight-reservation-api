import unittest
import json
from tests import BaseTestSetUp
from tests.test_users.data_source import *


class TestUserCase(BaseTestSetUp):

    def test_new_user_registration_works(self):
        """Test API can register new user successfully (POST request)"""

        response = self.testHelper.add_user(new_user)
        result = json.loads(response.data.decode())
        self.assertEqual(result[
            "message"], "Registration successfull. Please log in")
        self.assertEqual(response.status_code, 201)
    
    def test_duplicate_user_registration_works(self):
        """Test API cannot register user with same email twice successfully (POST request)"""

        self.new_user = self.testHelper.add_user(new_user)
        response = self.testHelper.add_user(duplicate_user)
        result = json.loads(response.data.decode())
        self.assertEqual(result[
            "message"], "User already exists. Please login")
        self.assertEqual(response.status_code, 409)
    
    def test_user_cannot_register_with_blank_username(self):
        """Test API cannot register user with blank username (POST request)"""

        response = self.testHelper.add_user(user_missing_name)
        result = json.loads(response.data.decode())
        self.assertEqual(result[
            "message"], "username is required field")
        self.assertEqual(response.status_code, 409)
    
    def test_user_cannot_register_with_blank_email(self):
        """Test API cannot register user with blank email (POST request)"""

        response = self.testHelper.add_user(user_missing_email)
        result = json.loads(response.data.decode())
        self.assertEqual(result[
            "message"], "email is required field")
        self.assertEqual(response.status_code, 409)

    def test_user_cannot_register_with_blank_password(self):
        """Test API cannot register user with blank password (POST request)"""

        response = self.testHelper.add_user(user_missing_password)
        result = json.loads(response.data.decode())
        self.assertEqual(result[
            "message"], "password is required field")
        self.assertEqual(response.status_code, 409)

    def test_user_cannot_register_with_invalid_username(self):
        """Test API cannot register user with invalid username (POST request)"""

        response = self.testHelper.add_user(invalid_username)
        result = json.loads(response.data.decode())
        self.assertEqual(result[
            "message"], "Invalid username")
        self.assertEqual(response.status_code, 409)

    def test_user_cannot_register_with_invalid_email(self):
        """Test API cannot register user with invalid email (POST request)"""

        response = self.testHelper.add_user(invalid_email)
        result = json.loads(response.data.decode())
        self.assertEqual(result[
            "message"], "Invalid email")
        self.assertEqual(response.status_code, 409)

    def test_user_cannot_register_with_invalid_password(self):
        """Test API cannot register user with invalid password (POST request)"""

        response = self.testHelper.add_user(invalid_password)
        result = json.loads(response.data.decode())
        self.assertEqual(result[
            "message"], "Invalid password")
        self.assertEqual(response.status_code, 409)

    def test_user_cannot_register_with_blank_username_key(self):
        """Test API cannot register user with blank username key (POST request)"""

        response = self.testHelper.add_user(missing_username_key)
        result = json.loads(response.data.decode())
        self.assertEqual(result[
            "message"], "username key is missing")
        self.assertEqual(response.status_code, 409)

    def test_user_cannot_register_with_blank_email_key(self):
        """Test API cannot register user with blank email key (POST request)"""

        response = self.testHelper.add_user(missing_email_key)
        result = json.loads(response.data.decode())
        self.assertEqual(result[
            "message"], "email key is missing")
        self.assertEqual(response.status_code, 409)

    def test_user_cannot_register_with_blank_password_key(self):
        """Test API cannot register user with blank password key (POST request)"""

        response = self.testHelper.add_user(missing_password_key)
        result = json.loads(response.data.decode())
        self.assertEqual(result[
            "message"], "password key is missing")
        self.assertEqual(response.status_code, 409)

    def test_user_cannot_register_with_special_character(self):
        """Test API cannot register user with special characters for username (POST request)"""

        response = self.testHelper.add_user(special_username)
        result = json.loads(response.data.decode())
        self.assertEqual(result[
            "message"], "Invalid username")
        self.assertEqual(response.status_code, 409)

    def test_user_cannot_register_with_email_with_spaces(self):
         """Test API cannot register user with email with spaces (POST request)"""

         response = self.testHelper.add_user(email_with_spaces)
         result = json.loads(response.data.decode())
         self.assertEqual(result[
            "message"], "Invalid email")
         self.assertEqual(response.status_code, 409)