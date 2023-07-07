import sys
sys.path.append(r"R:\Pro\Python\coursework_3_source\project\dao\base.py")
sys.path.append(r"R:\Pro\Python\coursework_3_source\project\dao\models\genres.py")
from project.dao.base import BaseDAO
from flask_sqlalchemy import BaseQuery

from flask import request
from werkzeug.exceptions import NotFound
from sqlalchemy import desc

from project.dao.models.genres import Genre
from project.dao.models.directors import Director
from project.dao.models.movies import Movie
from project.dao.models.users import User



class GenresDAO(BaseDAO[Genre]):
    __model__ = Genre
    
    

class MoviesDAO(BaseDAO[Movie]):
    __model__ = Movie

    def get_new(self,page):
        stmt: BaseQuery = self._db_session.query(self.__model__).order_by(desc(self.__model__.year))
        if page:
            try:
                return stmt.paginate(page, self._items_per_page).items
            except NotFound:
                return []
        return stmt.all()

class DirectorsDAO(BaseDAO[Director]):
    __model__ = Director
    
    
class UsersDAO(BaseDAO[User]):
    __model__ = User


    def get_by_email(self, email):
        email = User.query.filter(User.email == email).first()
        return email


    def register_user(self):
        req_json = request.json
        user = User(**req_json)
        self._db_session.add(user)
        self._db_session.commit()
        return user
        

    def patch_user(self, user_id):
        user = User.query.get(user_id)
        req_json = request.json
        user.name = req_json.get("name")
        user.surname = req_json.get("surname")
        self._db_session.add(user)
        self._db_session.commit()
        return "Пользователь обновлён"

    def password_change(self, user, new_password):
        user.password = new_password
        self._db_session.add(user)
        self._db_session.commit()
        return "Смена пароля прошла успешно"
    

    def added_movie_by_user(self, movie_id):
        movie = Movie.query.get(movie_id)
        movie_genre = movie.genre_id
        user_id = request.json.get('user_id')
        user = UsersDAO.get_by_id(user_id)
        user.favorite_genre = movie_genre
        self._db_session.add(user)
        self._db_session.commit()
        return "Фильм успешно добавлен"
    


