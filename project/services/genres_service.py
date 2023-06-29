
from project.dao.main import GenresDAO
from project.exceptions import ItemNotFound



class GenresService:
    def __init__(self, dao: GenresDAO):
        self.dao = dao

    def get_item(self, id):
        if genre := self.dao.get_by_id(id):
            return genre
        raise ItemNotFound(f'Жанр с таким id={id} не найден.')

    def get_all(self, page):
        return self.dao.get_all(page)
