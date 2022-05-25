from flask_restx import Resource, Namespace

from dao.model.directors import DirectorSchema
from implemented import directors_service

directors_ns = Namespace("directors")

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@directors_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        directors = directors_service.get_all()
        return directors_schema.dump(directors), 200


@directors_ns.route('/<int:id>')
class DirectorView(Resource):
    def get(self, id):
        director = directors_service.get_one(id)
        if director is None:
            return 'Movie not found', 404
        return director_schema.dump(director), 200
