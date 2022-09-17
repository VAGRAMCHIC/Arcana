from . import gallery_bp
from .models import *
from ..extentions import db

from flask import redirect, jsonify
from flask_restx import Api, Resource, fields
import jwt

@gallery_bp.route('/')
def index():
    #material = Material.query.all()
    #material_responce= MaterialSchema(many=True)
    #items = Item.query.all()
    #items_responce = ItemSchema(many=True)
    #return jsonify({'items': items_responce.dump(items), 'material':material_responce.dump(material)})
    return 'aboba'


