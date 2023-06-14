from typing import Optional


from project.dao.main import MoviesDAO
from project.exceptions import BaseServiceError, ItemNotFound
from project.dao.models.movies import Movie

from flask import request

class MoviesService():
    def __init__(self, dao: MoviesDAO) -> None:
        self.dao = dao
        
        
    def get_by_id(self, id):
        if movie := self.dao.get_by_id(id):
            return movie
        raise ItemNotFound(f'Фильм с таким id={id} не найден.')
        
    def get_all(self, page: Optional[int] = None) -> list[Movie]:
        
        return self.dao.get_all(page=page)
    
    def get_new(self, page: Optional[int] = None) -> list[Movie]:
        request_data = request.args
        if 'status' in request_data:
            if request_data['status'] == 'new':
                return self.dao.get_new(page)
        
        