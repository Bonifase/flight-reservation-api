from flights import db
from flask_bcrypt import Bcrypt
from flights.models.validate_fields import *
from flights.models.flight import *
from helpers.create_object import *

from sqlalchemy.ext.hybrid import hybrid_property

class User(db.Model):
    """This class defines the users table """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    _username = db.Column("username", db.String(80))
    _email = db.Column("email", db.String(120), unique=True)
    _password = db.Column("password", db.String(80))
    _passport = db.Column("passport", db.String(80))
    _isAdmin = db.Column("isAdmin", db.Boolean)

    def __init__(self, username=None, email=None, password=None, passport=None,
    isAdmin=None):
        self.username = username
        self.email = email
        self.password = password
        self.passport = passport
        self.isAdmin = isAdmin

    def save_item(self):
        return create_object(self, db)

    @hybrid_property
    def username(self):
        """defines username attribute for user object"""
        return self._username

    @username.setter
    def username(self, value):
        """validates with predefined patterns"""
        match = name_pattern(value)
        if match:
            self._username = value
            return
        assert 0, 'Invalid username'
    
    @hybrid_property
    def isAdmin(self):
        """defines is_admin attribute for user object"""
        return self._isAdmin

    @isAdmin.setter
    def isAdmin(self, value):
        self._isAdmin = value
            
    @hybrid_property
    def email(self):
        """defines an email attribute for user object"""
        return self._email

    @email.setter
    def email(self, value):
        """validates with predefined patterns and sets 
        an email attribute for user object"""
        match = email_pattern(value)
        if match:
            self._email = value
            return
        assert 0, 'Invalid email'
 
    @hybrid_property
    def password(self):
        """defines password attribute for user object"""
        return self._password

    @password.setter
    def password(self, value):
        """validates with predefined patterns and sets 
        password attribute for user object"""
        match = password_pattern(value)
        if match:
            self._password = Bcrypt().generate_password_hash(value).decode()
            return
        assert 0, 'Invalid password'
    
    @hybrid_property
    def passport(self):
        """defines passport attribute for user object"""
        return self._passport

    @passport.setter
    def passport(self, value):
        self._passport = value
    
