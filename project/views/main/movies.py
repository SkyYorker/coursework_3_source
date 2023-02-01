from flask_restx import Namespace, Resource

from project.container import movie_service
from project.setup.api.models import movie
from project.setup.api.parsers import page_parser

from flask import request

api = Namespace('movies')


@api.route("/")
class MoviesViews(Resource):
    @api.expect(page_parser)
    @api.marshal_with(movie, as_list=True, code=200, description='OK')
    def get(self):
        if request.args:
            return movie_service.get_new(**page_parser.parse_args())
           
        return movie_service.get_all(**page_parser.parse_args())
    



@api.route('/<int:movie_id>/')
class MoviesView(Resource):
    @api.response(404, 'Not Found')
    @api.marshal_with(movie, as_list=True, code=200, description='OK')
    def get(self, movie_id: int):
        """
        Get genre by id.
        """
        return movie_service.get_by_id(movie_id)