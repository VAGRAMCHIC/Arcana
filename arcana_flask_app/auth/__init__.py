from flask.blueprints import Blueprint


auth_bp = Blueprint('auth', __name__, static_folder='static')

from .routes import *