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
    # role = Column(String(100))
    
# class DirectorSchema(Schema):
#     id = fields.Integer()
#     email = fields.String()
#     password = fields.String()
#     name = fields.String()
#     surname = fields.String()
#     favorite_genre  = fields.String()


