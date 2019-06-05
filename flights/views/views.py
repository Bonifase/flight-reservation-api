from flights import app
from flask import request, jsonify
from flights.models.user import User
from validators.validator import validate_data


@app.route('/api/user/register', methods=['POST'])
def register():
    data = request.get_json()
    user = {
        'username': data.get('username'),
        'email': data.get('email'),
        'password': data.get('password')}
    try:
        validated_data = validate_data(**user)
    except AssertionError as error:
        return jsonify({'message': error.args[0]}), 409
    if validated_data:
        users = User.query.all()
        available_emails = [user.email for user in users]

        if validated_data.get('email') in available_emails:
            return jsonify({
                "message": "User already exists. Please login"}), 409
        else:
            try:
                user = User(
                    validated_data['username'],
                    validated_data['email'], 
                    validated_data['password'])
                user.register_user()
            except AssertionError as err:
                return jsonify({'message': err.args[0]}), 409
        return jsonify({
            "message": "Registration successfull. Please log in"}), 201