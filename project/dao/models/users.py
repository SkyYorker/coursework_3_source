from sqlalchemy import Column, String, Integer
from project.setup.db import db
from marshmallow import Schema, fields

class User(db.Model):
    __tablename__ = "users"
    id = Column(Integer(100))
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