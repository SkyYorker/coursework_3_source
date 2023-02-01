from flask import current_app
from project.tools.security import generate_password_digest, generate_password_hash
from project.services.users_service import UserService
import jwt


class AuthService:
    def __init__(self, user_service: UserService) -> None:
        self.user_service = user_service


    def generate_token(self, name):
        user = self.user_service.get_by_username(name)
        
        if not user:
            raise Exception("Не найден пользователь")
        