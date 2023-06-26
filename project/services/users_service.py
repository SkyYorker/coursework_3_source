from project.dao.main import UsersDAO
from project.exceptions import BaseServiceError, ItemNotFound


from project.tools.security import generate_password_digest, generate_password_hash

from flask import request




class UsersService:
    def __init__(self, dao: UsersDAO) -> None:
        self.user_dao = dao
        
        
    def get_by_email(self, email):
        return self.user_dao.get_by_email(email)


    def add_user(self, user):
        user["password"] = generate_password_digest(user["password"])
        return self.user_dao.register_user()


    def get_by_id(self, id):
        if user := self.user_dao.get_by_id(id):
            return user
        raise ItemNotFound(f'Пользователь с таким id={id} не найден.')


    def patch_user(self, id):
        if _ := self.user_dao.get_by_id(id):
            return self.user_dao.patch_user(id)
        raise ItemNotFound(f'Пользователь с таким id={id} не найден.')

    
    def password_change(self, old_password, email, new_password):
        if email := self.user_dao.get_by_email(email):
            if generate_password_hash(old_password) == email.password:
                password = generate_password_hash(new_password)
                return self.user_dao.password_change(email, password)
        raise ItemNotFound(f'Пользователь с такой почтой={email} не найден.')