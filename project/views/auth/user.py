from flask_restx import Namespace, Resource

from project.container import user_service
from project.setup.api.models import user

from flask import request

api = Namespace('user')



@api.route('/<int:user_id>')
class UserView(Resource):
    @api.response(404, 'Not Found')
    @api.marshal_with(user, as_list=True, code=200, description='OK')
    def get(self, user_id: int):
        
        user = user_service.get_by_id(user_id)
        return user


@api.route('/user/<int:user_id>')
class UserView(Resource):
    methods = ['PATCH']
    def patch(self, user_id):
        
        
        return user_service.patch_user(user_id)
        


@api.route('/user/password/<int:user_id>')
class UserView(Resource):
    def put(self, user_id):
        req_json = request.json
        password_1 = req_json.get("password_1")
        password_2 = req_json.get("password_2")
        user_service.password_change(password_1, password_2, user_id)
        pass 