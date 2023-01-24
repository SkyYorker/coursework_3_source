import sys
sys.path.append(r"D:\Pro\Python\coursework_3_source\project\dao\base.py")
sys.path.append(r"D:\Pro\Python\coursework_3_source\project\dao\models\genres.py")
from project.dao.base import BaseDAO
from project.dao.models.genres import Genre


class GenresDAO(BaseDAO[Genre]):
    __model__ = Genre
