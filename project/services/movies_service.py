from typing import Optional


from project.dao.base import BaseDAO
from project.exceptions import BaseServiceError, ItemNotFound
from project.dao.models.movies import Movie



class MoviesService():
    def __init__(self, dao: BaseDAO) -> None:
        self.dao = dao
        
        
    def get_by_id(self, id):
        return self.get_by_id(id)
        
    def get_all(self, page: Optional[int] = None) -> list[Movie]:
        return self.dao.get_all(page=page)