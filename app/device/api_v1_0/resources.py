from flask import request, Blueprint
from flask_restful import Api, Resource

from .schemas import RatingSchema, StatusSchema
from ..models import Rating, Status
from ...data_source import DataSource

## RATING RESOURCE
rating_v1_0_bp = Blueprint('rating_v1_0_bp', __name__)
rating_schema = RatingSchema()
api = Api(rating_v1_0_bp)

class RatingResource(Resource):
    def get(self):
        rating = DataSource().getRating()
        result = rating_schema.dump(rating, many=False)
        return result

api.add_resource(RatingResource, '/api/v1.0/rating/', endpoint='rating_resource')


## STATUS RESOURCE
status_v1_0_bp = Blueprint('status_v1_0_bp', __name__)
status_schema = StatusSchema()
api = Api(status_v1_0_bp)

class StatusResource(Resource):
    def get(self):
        status = DataSource().getStatus()
        result = status_schema.dump(status, many=False)
        return result
        
api.add_resource(StatusResource, '/api/v1.0/status/', endpoint='status_resource')