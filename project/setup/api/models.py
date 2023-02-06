from flask_restx import fields, Model

from project.setup.api import api

genre: Model = api.model('Жанр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Комедия'),
})


movie: Model = api.model('Фильм', {
    'id': fields.Integer(required=True, example=1),
    "title" : fields.String(required=True, max_length=100, example='Вооружен и очень опасен'),
    "trailer" : fields.String(required=True, max_length=100, example='https://www.youtube.com/watch?v=hLA5631F-jo'),
    "description" : fields.String(required=True, max_length=255, example='События происходят в конце XIX века на Диком Западе, в Америке. В основе сюжета — сложные перипетии жизни работяги — старателя Габриэля Конроя. Найдя нефть на своем участке, он познает и счастье, и разочарование, и опасность, и отчаяние...'),
    "year" : fields.Integer(required=True, max_length=100, example='1978'),
    "rating"  : fields.Integer(required=True, max_length=100, example='6'),
    "genre_id"  : fields.Integer(required=True, max_length=100, example='17'),
    "director_id"  : fields.Integer(required=True, max_length=100, example='3'),
})

director: Model = api.model('Режиссёр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Тейлор Шеридан'),
})


user: Model = api.model('Пользователь', {
    'id': fields.Integer(required=True, example=1),
    "email" : fields.String(required=True, max_length=100),
    "name" : fields.String(required=True, max_length=100),
    "surname" : fields.String(required=True, max_length=100),
    "favorite_genre"  : fields.String(required=True, max_length=100)
})
