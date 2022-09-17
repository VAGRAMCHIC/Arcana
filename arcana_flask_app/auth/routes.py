from hashlib import new
from . import auth_bp
from .models import User
from ..extentions import db

from flask import request, redirect, url_for, jsonify
from flask_restx import Api, Resource, fields
import jwt


rest_api = Api(version="1.0", title="Users API")

signup_model = rest_api.model(
    'SignUpModel', {
        "user_name": fields.String(required=True, min_length=2, max_length=32),
        "email": fields.String(required=True, min_length=4, max_length=64),
        "password": fields.String(required=True, min_length=4, max_length=16)
    }
)

@auth_bp.route('/login')
def login():
    return 'login'

@auth_bp.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        req_data = request.get_json()
        _email = req_data.get('email')
        _user_name = req_data.get('user_name')
        _password = req_data.get('password')

        user_exists = User.get_by_email(_email)
        if user_exists:
            return {"succcess":False,
                        "msg":"Email already taken"}, 400
        new_user = User(user_name=_user_name, email=_email)
        new_user.password.set(_password)
        new_user.save()
        
        return {
            "success": True,
            "userID": new_user.id,
            "msg": "Пользователь успешно зарегистрирован"
        }, 200

    return 'Signup'

@auth_bp.route('/logout')
def logout():
    return 'Logout'


@auth_bp.route('/profile')
def profile():
    return 'profile'