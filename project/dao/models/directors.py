from sqlalchemy import Column, String, Integer
from project.setup.db import models
from marshmallow import Schema, fields

class Director(models.Base):
    __tablename__ = "director"
    name = Column(String(255), unique=True)
    
    
class DirectorSchema(Schema):
    id = fields.Int
    name = fields.Str