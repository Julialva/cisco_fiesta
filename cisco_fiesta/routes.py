

from cisco_fiesta import api
from flask_restful import Resource
from cisco_fiesta.core.reader import get_source_file


class get_main_tables(Resource):
    def get(self,main_name_list,col_list):
        return {"data" : get_source_file(eval(main_name_list),eval(col_list))}
class get_ft_tables(Resource):
    def get(self,ft_name_list,ft_col_list):
        return {"data" : get_source_file(eval(ft_name_list),eval(ft_col_list),fast_track=True)}

api.add_resource(get_main_tables, "/tables/<string:main_name_list>/<string:col_list>")
api.add_resource(get_ft_tables, "/fastables/<string:ft_name_list>/<string:ft_col_list>")