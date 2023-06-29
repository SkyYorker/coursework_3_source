from project.dao import GenresDAO
from project.dao.main import MoviesDAO
from project.dao.main import DirectorsDAO
from project.dao.main import UsersDAO
from project.dao.main import FavoriteDAO

from project.services import DirectorsService
from project.services import GenresService
from project.services import MoviesService
from project.services import UsersService
from project.services import AuthService
from project.services import FavoriteService


from project.setup.db import db

# DAO
genre_dao = GenresDAO(db.session)
movie_dao = MoviesDAO(db.session)
director_dao = DirectorsDAO(db.session)
user_dao = UsersDAO(db.session)
favorite_dao = FavoriteDAO(db.session)

# Services
genre_service = GenresService(dao=genre_dao)
movie_service = MoviesService(dao=movie_dao)
director_service = DirectorsService(dao=director_dao)
user_service = UsersService(dao=user_dao)
auth_service = AuthService(dao=user_service)
favortie_service = FavoriteService(dao=favorite_dao)