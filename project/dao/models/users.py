from sqlalchemy import Column, String
from project.setup.db import models
from marshmallow import Schema, fields

class User(models.Base):
    __tablename__ = "user"
    email = Column(String(100), unique=True)
    password = Column(String(100))
    name = Column(String(100))
    surname = Column(String(100))
    favorite_genre  = Column(String(100))
    
    
class DirectorSchema(Schema):
    id = fields.Int
    email = fields.Str
    password = fields.Str
    name = fields.Str
    surname = fields.Str
    favorite_genre  = fields.Str