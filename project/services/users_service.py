from project.dao.main import UsersDAO
from project.exceptions import BaseServiceError, ItemNotFound


from project.tools.security import generate_password_digest, generate_password_hash

from flask import request




class UsersService:
    def __init__(self, dao: UsersDAO) -> None:
        self.user_dao = dao
        
        
    def get_by_email(self, email):
        self.user_dao.get_by_email(email)


    def add_user(self, user):
        user["password"] = generate_password_digest(user["password"])
        return self.user_dao.register_user()