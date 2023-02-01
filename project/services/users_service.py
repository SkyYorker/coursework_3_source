from project.dao.base import BaseDAO
from project.exceptions import BaseServiceError, ItemNotFound
from project.dao.models.users import User





class UserService:
    def __init__(self, user_dao: BaseDAO) -> None:
        self.user_dao = user_dao
        
        
    def get_by_username(self, name):
        self.user_dao.get_by_username(name)