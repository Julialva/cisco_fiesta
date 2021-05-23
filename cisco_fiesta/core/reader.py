from cisco_fiesta.ports.data_fetch_port import XlsxPort
from cisco_fiesta.ports.data_fetch_port import ScrappPort

def update_source_file():
    file_finder = ScrappPort()
    file_finder.scrapp_data()

def read_source_file(main_name_list,col_list,fast_track=False,sheet_dict=dict()):
    file_reader = XlsxPort()
    file_dict = file_reader.fetch_data(main_name_list,col_list,fast_track=fast_track,sheet_dict=sheet_dict)
    return file_dict
