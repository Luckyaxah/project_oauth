from flask import Blueprint, jsonify
from flask_cors import CORS

api_v1 = Blueprint('api_v1', __name__)

CORS(api_v1)


from project_oauth.apis.v1 import resources