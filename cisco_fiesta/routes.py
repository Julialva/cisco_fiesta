

# from cisco_fiesta.db_models.db_models import task
from cisco_fiesta import api
from flask_restful import Resource
from cisco_fiesta.core.reader import update_source_file,read_source_file


class get_main_tables(Resource):
    def get(self,main_name_list,col_list):
        return {"data" : read_source_file(eval(main_name_list),eval(col_list))}
class get_ft_tables(Resource):
    def get(self,ft_name_list,ft_col_list):
        return {"data" : read_source_file(eval(ft_name_list),eval(ft_col_list),fast_track=True)}
class update_source_tables(Resource):
    def put(self):
        update_source_file()
        return {"message": "input_file updated."}, 204


api.add_resource(get_main_tables, "/tables/<string:main_name_list>/<string:col_list>")
api.add_resource(get_ft_tables, "/fastables/<string:ft_name_list>/<string:ft_col_list>")
api.add_resource(update_source_tables,"/update")