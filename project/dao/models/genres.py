from sqlalchemy import Column, String

from project.setup.db import models

from marshmallow import Schema,fields

class Genre(models.Base):
    __tablename__ = 'genre'
    name = Column(String(100), unique=True, nullable=False)



# class DirectorSchema(Schema):
#     id = fields.Int
#     name = fields.Str