from .genres import api as genres_ns
from .movies import api as movies_ns
from .directors import api as directors_ns
from ..auth.auth import api as auth_ns

__all__ = [
    'genres_ns',
    'movies_ns',
    'directors_ns',
    'auth_ns',
]
