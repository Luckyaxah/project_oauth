from flask import jsonify, request
from flask.views import MethodView

from project_oauth.apis.v1 import api_v1
from project_oauth.apis.v1.auth import generate_token
from project_oauth.models import User



@api_v1.route('/hello')
def hello():
    return jsonify(message='hello, world')
class IndexAPI(MethodView):

    def get(self):
        return jsonify({
            "api_version": "1.0",
            "api_base_url": "http://project_oauth.com/api/v1",
            "current_user_url": "http://project_oauth.com/api/v1/user",
            "authentication_url": "http://project_oauth.com/api/v1/token",
            "item_url": "http://project_oauth.com/api/v1/items/{item_id }",
            "current_user_items_url": "http://project_oauth.com/api/v1/user/items{?page,per_page}",
            "current_user_active_items_url": "http://project_oauth.com/api/v1/user/items/active{?page,per_page}",
            "current_user_completed_items_url": "http://project_oauth.com/api/v1/user/items/completed{?page,per_page}",
        })

class AuthTokenAPI(MethodView):
    def post(self):
        grant_type = request.form.get('grant_type')
        username = request.form.get('username')
        password = request.form.get('password')

        if grant_type is None or grant_type.lower() != 'password':
            return api_abort(code=400, message='The grant type must be password.')
        
        user = User.query.filter_by(username=username).first()
        if user is None or not user.validate_password(password):
            return api_abort(code=400, message='Either the username or password was invalid.')
        token, expiration = generate_token(user)

        response = jsonify({
            'access_token': token,
            'token_type': 'Bearer',
            'expires_in': expiration
        })
        response.headers['Cache-Control'] = 'no-store'
        response.headers['Pragma'] = 'no-cache'
        return response

api_v1.add_url_rule('/', view_func=IndexAPI.as_view('index_api'), methods=['GET'])
api_v1.add_url_rule('/oauth/token', view_func=AuthTokenAPI.as_view('oauth_api'), methods=['POST'])