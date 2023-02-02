from typing import Optional

from project.dao.main import GenresDAO
from project.exceptions import ItemNotFound
from project.dao.models.genres import Genre


class GenresService:
    def __init__(self, dao: GenresDAO) -> None:
        self.dao = dao

    def get_item(self, pk: int) -> Genre:
        if genre := self.dao.get_by_id(pk):
            return genre
        raise ItemNotFound(f'Жанр с таким id={id} не найден.')

    def get_all(self, page: Optional[int] = None) -> list[Genre]:
        return self.dao.get_all(page=page)
