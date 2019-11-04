from flights import app
from flask import request, jsonify
from flask_jwt_extended import (
    JWTManager, jwt_required, get_jwt_identity,
    create_access_token,  decode_token, get_raw_jwt
)

from flights.controller.user_controller import UserController

jwt = JWTManager(app)

blacklist = set()
stored_reset_tokens = set()


@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return jti in blacklist


@app.route('/api/user/register', methods=['POST'])
def register():
    return UserController.register_controller()
    
@app.route('/api/user/login', methods=['POST'])
def login():
    return UserController.login_controller()

@app.route('/api/user/logout', methods=['POST'])
@jwt_required
def logout():
    jti = get_raw_jwt()['jti']
    blacklist.add(jti)
    return jsonify({"message": "Logout Successful"}), 200