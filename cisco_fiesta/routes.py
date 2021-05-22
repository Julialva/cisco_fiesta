

from cisco_fiesta import api
from flask_restful import Resource
from cisco_fiesta.core.reader import test_func


class get_last_tables(Resource):
    def get(self):
        test_exit = test_func()
        return {"data" : test_exit}
api.add_resource(get_last_tables, "/tables")
