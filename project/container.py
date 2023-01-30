from project.dao import GenresDAO
from project.dao.main import MoviesDAO

from project.services import GenresService
from project.services import MoviesService
from project.setup.db import db

# DAO
genre_dao = GenresDAO(db.session)
movie_dao = MoviesDAO(db.session)

# Services
genre_service = GenresService(dao=genre_dao)
movie_service = MoviesService(dao=movie_dao)
