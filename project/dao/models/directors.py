from sqlalchemy import Column, String
from project.setup.db import db
from marshmallow import Schema, fields

class Director(db.Model):
    __tablename__ = "directors"
    name = Column(String(100))
    
    
class DirectorSchema(Schema):
    name = fields.Str