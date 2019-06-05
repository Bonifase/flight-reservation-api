from flights import app
from flask import request, jsonify
from flask_jwt_extended import (
    JWTManager, jwt_required, get_jwt_identity,
    create_access_token,  decode_token, get_raw_jwt
)
from flask_bcrypt import Bcrypt
from flights.models.user import User
from validators.validator import validate_data

jwt = JWTManager(app)

blacklist = set()
stored_reset_tokens = set()


@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return jti in blacklist


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


@app.route('/api/user/login', methods=['POST'])
def login():
    data = request.get_json()
    user = {
        'email': data.get('email'),
        'password': data.get('password')}
    try:
        validated_data = validate_data(**user)
    except AssertionError as error:
        return jsonify({'message': error.args[0]}), 409
    if validated_data:
        user = User.query.filter_by(email=validated_data ["email"]).first()
        if user:
            if Bcrypt().check_password_hash(
                user.password, validated_data["password"]):
                access_token = create_access_token(identity=user.id)           
                if access_token:
                    response = {
                                'message': 'You logged in successfully.',
                                '_id': user.id,
                                'username': user.username,
                                'email': user.email,
                                'AuthToken': access_token
                            }
                return jsonify(response), 200

            else:
                return jsonify({"message": "wrong password"}), 409

        else:
            return jsonify({"message": "Invalid email, Please try again"}), 409

@app.route('/api/user/logout', methods=['POST'])
@jwt_required
def logout():
    jti = get_raw_jwt()['jti']
    blacklist.add(jti)
    return jsonify({"message": "Logout Successful"}), 200