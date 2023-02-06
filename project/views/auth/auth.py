from flask_restx import Namespace, Resource

from project.container import user_service
from project.container import auth_service

from project.setup.api.models import user

from flask import request

api = Namespace('auth')


@api.route('/register')
class AuthView(Resource):
    def post(self):
        req_json = request.json
        user = user_service.add_user(req_json)
        return "Пользователь добавлен", 201, {"location": f"/users/{user.id}"}


@api.route('/login')
class AuthView(Resource):
    def post(self):
        req_json = request.json
        email = req_json.get("email")
        password = req_json.get("password")
        if not(email or password):
            return "Нужнен логин и пароль", 400

        tokens = auth_service.generate_token(email, password)
        if tokens:
            return tokens
        else:
            return "Хрен тебе", 400


    def put(self):
        req_json = request.json
        ref_token = req_json.get('refresh_token')       
        tokens = auth_service.refresh_token(ref_token)
        if tokens:
            return tokens
        else:
            return "Хрен тебе", 400