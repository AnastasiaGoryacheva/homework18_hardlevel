from flask import request
from flask_restx import Resource, Namespace
from marshmallow.exceptions import ValidationError
from sqlalchemy.exc import NoResultFound

from dao.model.movies import MovieSchema
from implemented import movies_service

movies_ns = Namespace("movies")

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movies_ns.route('/')
class MoviesView(Resource):
    def get(self):
        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')
        year = request.args.get('year')

        if year:
            movies = movies_service.get_by_year(year)
        elif director_id:
            movies = movies_service.get_by_director(director_id)
        elif genre_id:
            movies = movies_service.get_by_genre(genre_id)
        else:
            movies = movies_service.get_all()

        return movies_schema.dump(movies), 200

    def post(self):
        req_json = request.json
        try:
            movies_service.create(req_json)
            return "", 201
        except ValidationError as e:
            return f"{e}", 400


@movies_ns.route('/<int:id>')
class MovieView(Resource):
    def get(self, id):
        movie = movies_service.get_one(id)
        if movie is None:
            return 'Movie not found', 404
        return movie_schema.dump(movie), 200

    def put(self, id):
        req_json = request.json
        req_json["id"] = id
        try:
            movies_service.update(req_json)
            return "", 204
        except ValidationError as e:
            return f"{e}", 400

    def delete(self, id):
        try:
            movies_service.delete(id)
            return "", 204
        except NoResultFound as e:
            return str(e), 404
