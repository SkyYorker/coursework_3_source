from typing import Optional


from project.dao.main import DirectorsDAO
from project.exceptions import BaseServiceError, ItemNotFound
from project.dao.models.directors import Director



class DirectorsService():
    def __init__(self, dao: DirectorsDAO) -> None:
        self.dao = dao
        
        
    def get_by_id(self, id):
        if director := self.dao.get_by_id(id):
            return director
        raise ItemNotFound(f'Режиссёр с таким id={id} не найден.')
        
    def get_all(self, page: Optional[int] = None) -> list[Director]:
        return self.dao.get_all(page)