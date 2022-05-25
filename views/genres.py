from flask_restx import Resource, Namespace

from dao.model.genres import GenreSchema
from implemented import genres_service

genres_ns = Namespace("genres")

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genres_ns.route('/')
class GenresView(Resource):
    def get(self):
        genres = genres_service.get_all()
        return genres_schema.dump(genres), 200


@genres_ns.route('/<int:id>')
class GenreView(Resource):
    def get(self, id):
        genre = genres_service.get_one(id)
        if genre is None:
            return 'Movie not found', 404
        return genre_schema.dump(genre), 200
