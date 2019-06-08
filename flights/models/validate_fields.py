import re


def name_pattern(value):
    pattern = r'[a-zA-Z]{3,8}'
    match = re.search(pattern, value)
    return match

"""A method that checks departure and arrival time patterns"""


def time_pattern(value):
    pattern = '^\d\d\d\d/(0?[1-9]|1[0-2])/(0?[1-9]|[12][0-9]|3[01]) (00|[0-9]|1[0-9]|2[0-3]):([0-9]|[0-5][0-9]):([0-9]|[0-5][0-9])$'
    match = re.search(pattern, value)
    return match
"""A method that checks email patterns"""


def email_pattern(value):
    pattern = r'[a-zA-Z0-9_\.&-]{4,30}@[a-z]+\..'
    match = re.search(pattern, value)
    return match
"""A method that checks password patterns"""


def password_pattern(value):

    pattern = r'[a-zA-Z0-9_@&\.]{6,20}'
    match = re.search(pattern, value)
    return match


def attribute_pattern(value):
    pattern = r'[a-zA-Z]{2,8}'
    match = re.search(pattern, value)
    return match

def number_pattern(value):
    pattern = r'[A-Z0-9]{2,8}'
    match = re.search(pattern, value)
    return match