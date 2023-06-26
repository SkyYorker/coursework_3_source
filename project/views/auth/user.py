from flask_restx import Namespace, Resource
from flask import current_app
from flask import request

from project.container import user_service
from project.setup.api.models import user

import jwt

api = Namespace('user')



@api.route('/<int:user_id>')
class UserView(Resource):
    @api.response(404, 'Not Found')
    @api.marshal_with(user, as_list=True, code=200, description='OK')
    def get(self, user_id: int):
        
        user = user_service.get_by_id(user_id)
        return user


@api.route('/<int:user_id>')
class UserView(Resource):
    methods = ['PATCH']
    def patch(self, user_id: int):
        
        
        return user_service.patch_user(user_id)
        


@api.route('/password/')
class UserView(Resource):
    def put(self):
        req_json = request.json
        token = request.headers['Authorization'].split()[1]
        data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
        email = req_json.get("email")
        old_password = req_json.get("old_password")
        new_password = req_json.get('new_password')
        # user_service.password_change(old_password, email, new_password)
        return user_service.password_change(old_password, email, new_password) 