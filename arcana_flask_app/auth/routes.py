from . import auth_bp
from .models import User
from ..extentions import db

from flask import redirect, url_for, jsonify

@auth_bp.route('/login')
def login():
    return 'login'

@auth_bp.route('/signup', methods=['POST'])
def signup():
    return 'Signup'

@auth_bp.route('/logout')
def logout():
    return 'Logout'