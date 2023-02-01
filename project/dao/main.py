import sys
sys.path.append(r"D:\Pro\Python\coursework_3_source\project\dao\base.py")
sys.path.append(r"D:\Pro\Python\coursework_3_source\project\dao\models\genres.py")
from project.dao.base import BaseDAO
from project.dao.models.genres import Genre
from project.dao.models.directors import Director
from project.dao.models.movies import Movie
from project.dao.models.users import User

class GenresDAO(BaseDAO[Genre]):
    __model__ = Genre
    
    

class MoviesDAO(BaseDAO[Movie]):
    __model__ = Movie



class DirectorsDAO(BaseDAO[Director]):
    __model__ = Director
    
    
class UsersDAO(BaseDAO[User]):
    __model__ = User