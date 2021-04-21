from flask import jsonify
from flask.views import MethodView

from anotherme.apis.v1 import api_v1

@api_v1.route('/hello')
def hello():
    return jsonify(message='hello, world')
class IndexAPI(MethodView):

    def get(self):
        return jsonify({
            "api_version": "1.0",
            "api_base_url": "http://anotherme.com/api/v1",
            "current_user_url": "http://anotherme.com/api/v1/user",
            "authentication_url": "http://anotherme.com/api/v1/token",
            "item_url": "http://anotherme.com/api/v1/items/{item_id }",
            "current_user_items_url": "http://anotherme.com/api/v1/user/items{?page,per_page}",
            "current_user_active_items_url": "http://anotherme.com/api/v1/user/items/active{?page,per_page}",
            "current_user_completed_items_url": "http://anotherme.com/api/v1/user/items/completed{?page,per_page}",
        })

api_v1.add_url_rule('/', view_func=IndexAPI.as_view('index_api'), methods=['GET'])