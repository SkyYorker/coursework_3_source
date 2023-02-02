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
    @api.marshal_with(user)
    def post(self):
        req_json = request.json
        username = req_json.get("name")
        pasword = req_json.get("password")
        if not(username or pasword):
            return "Нужно имя и пароль", 400

        tokens = auth_service.generate_token(username, pasword)
        if tokens:
            return tokens
        else:
            return "Хрен тебе", 400
