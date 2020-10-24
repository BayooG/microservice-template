import logging

from flask import request
from flask_restx import Resource

from app.api.restx import api

log = logging.getLogger(__name__)
ns = api.namespace("test")

@ns.route('')
class TestCollection(Resource):
    
    def get(self):
        return {'msg':'hello'}, 200