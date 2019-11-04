import re


def name_pattern(value):
    pattern = r'[a-zA-Z]{3,8}'
    match = re.search(pattern, value)
    return match

def email_pattern(value):
    pattern = r'[a-zA-Z0-9_\.&-]{4,30}@[a-z]+\..'
    match = re.search(pattern, value)
    return match

def password_pattern(value):
    """A method that checks password patterns"""
    pattern = r'[a-zA-Z0-9_@&\.]{6,20}'
    match = re.search(pattern, value)
    return match

def number_pattern(value):
    pattern = r'[A-Z0-9]{2,8}'
    match = re.search(pattern, value)
    return match