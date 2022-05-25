from dao.directors import DirectorDAO
from dao.genres import GenreDAO
from dao.movies import MovieDAO
from service.directors import DirectorService
from service.genres import GenreService

from service.movies import MovieService
from setup_db import db

movies_dao = MovieDAO(db.session)
movies_service = MovieService(movies_dao)

directors_dao = DirectorDAO(db.session)
directors_service = DirectorService(directors_dao)

genres_dao = GenreDAO(db.session)
genres_service = GenreService(genres_dao)
