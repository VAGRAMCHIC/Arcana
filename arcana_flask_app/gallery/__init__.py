from flask.blueprints import Blueprint


gallery_bp = Blueprint('gallery', __name__, static_folder='static')

from .routes import *