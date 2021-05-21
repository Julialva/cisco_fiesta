

from cisco_fiesta import api
from flask_restful import Resource

class get_tables(Resource):
    def get(self):
        return {"data" : "should be tables but isn't"}
api.add_resource(get_tables, "/get_tables")
