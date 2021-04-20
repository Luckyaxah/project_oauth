from flask import Blueprint, jsonify

from anotherme.apis.v1 import resources
api_v1 = Blueprint('api_v1', __name__)


@api_v1.route('/')
def index():
    return jsonify(message='hello, world')