from flask import Flask
from flask_restx import Api

from config import Config
from dao.model.directors import Director
from dao.model.genres import Genre
from dao.model.movies import Movie
from setup_db import db
from views.directors import directors_ns
from views.genres import genres_ns
from views.movies import movies_ns


def create_app(config: Config) -> Flask:
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()
    return application


def configure_app(application: Flask):
    db.init_app(application)
    api = Api(app)

    api.add_namespace(movies_ns)
    api.add_namespace(directors_ns)
    api.add_namespace(genres_ns)


def load_data():
    director = Director(name='Кевин Файги')
    genre = Genre(name='Научная фантастика')
    movie = Movie(
        title='Мстители',
        description='Локи, сводный брат Тора, возвращается, и в этот раз он не один. '
                    'Земля оказывается на грани порабощения, и только лучшие из лучших могут спасти человечество.',
        trailer='https://www.youtube.com/watch?v=t6zLMSrmR-Y',
        year=2012,
        rating=8,
        genre_id=12,
        director_id=21
    )

    db.create_all()

    db.session.add(director)
    db.session.add(genre)
    db.session.add(movie)
    db.session.commit()
    db.session.close()


if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)
    configure_app(app)
    # load_data()  #функция наполнения бд, шаг 3.1 в дз (уже выполнен)
    app.run()
