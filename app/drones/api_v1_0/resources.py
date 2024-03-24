from flask import request, Blueprint
from flask_restful import Api, Resource
from app.common.error_handling import ObjectNotFound, AppErrorBaseClass
from .schemas import DroneSchema
from ..models import Drone, Rotor

drones_v1_0_bp = Blueprint('drones_v1_0_bp', __name__)
drone_schema = DroneSchema()
api = Api(drones_v1_0_bp)


class DroneListResource(Resource):
    def get(self):
        films = Drone.get_all()
        result = drone_schema.dump(films, many=True)
        return result

    def post(self):
        data = request.get_json()
        film_dict = drone_schema.load(data)
        film = Drone(name=film_dict['name'],
                     span=film_dict['span'],
                     created=film_dict['created'],
                     responsible=film_dict['responsible']
                     )
        for rotor in film_dict['rotors']:
            film.actors.append(Rotor(rotor['name']))
        film.save()
        resp = drone_schema.dump(film)
        return resp, 201


class DroneResource(Resource):
    def get(self, film_id):
        film = Drone.get_by_id(film_id)
        if film is None:
            raise ObjectNotFound("The drone doesn't exist")
        resp = drone_schema.dump(film)
        return resp


api.add_resource(DroneListResource, '/api/v1.0/drones/', endpoint='film_list_resource')
api.add_resource(DroneResource, '/api/v1.0/films/<int:film_id>', endpoint='film_resource')
