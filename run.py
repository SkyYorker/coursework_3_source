from project.config import config
from project.dao.models.genres import Genre
from project.dao.models.users import User
from project.server import create_app, db

app = create_app(config)


@app.shell_context_processor
def shell():
    return {
        "db": db,
        "Genre": Genre,
        "User": User
    }
