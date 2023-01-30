from sqlalchemy import Column, String, Integer, Float
from project.setup.db import models
from marshmallow import Schema, fields


class Movie(models.Base):
    __tablename__ = "movie"
    title = Column(String(225))
    trailer = Column(String(255))
    description = Column(String(255))
    year = Column(Integer)
    rating  = Column(Float(100))
    genre_id  = Column(Integer, models.db.ForeignKey('genre.id'))
    genre = models.db.relationship('Genre')
    director_id  = Column(Integer,models.db.ForeignKey('director.id'))
    director = models.db.relationship('Director')


class MovieSchema(Schema):
    id = fields.Int
    title = fields.Str
    trailer = fields.Str
    description = fields.Str
    year = fields.Int
    rating  = fields.Int
    genre_id  = fields.Int
    director_id  = fields.Int