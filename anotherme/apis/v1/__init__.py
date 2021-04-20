from flask import Blueprint, jsonify
from flask_cors import CORS
from anotherme.apis.v1 import resources
api_v1 = Blueprint('api_v1', __name__)

CORS(api_v1)

@api_v1.route('/')
def index():
    return jsonify(message='hello, world')