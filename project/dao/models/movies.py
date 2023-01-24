from sqlalchemy import Column, String, Integer, Float
from project.setup.db import db
from marshmallow import Schema, fields

class Movie(db.Model):
    __tablename__ = "movies"
    id = Column(Integer(100))
    title = Column(String(100))
    trailer = Column(String(100))
    description = Column(String(100))
    year = Column(Integer(100))
    rating  = Column(Float(100))
    genre_id  = Column(Integer(100))
    director_id  = Column(Integer(100))


class MovieSchema(Schema):
    id = fields.Int
    title = fields.Str
    trailer = fields.Str
    description = fields.Str
    year = fields.Int
    rating  = fields.FLoat
    genre_id  = fields.Int
    director_id  = fields.Int