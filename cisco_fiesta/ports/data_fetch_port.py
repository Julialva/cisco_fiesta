import json
from cisco_fiesta.adapters.excel_adapter import XlsReader
from cisco_fiesta.adapters.excel_adapter import FakeXlsReader
from cisco_fiesta.adapters.mail_adapter import MailScrapper
from cisco_fiesta.adapters.mail_adapter import FakeMailScrapper
import os

class ScrappPort(object):
    def __init__(self):
        self.adapter = eval(os.getenv('MAIL_ADAPTER'))()
    def scrapp_data(self):
        raw = self.adapter.find_mail()
        self.adapter.get_attachments(raw)
        
class XlsxPort(object):
    def __init__(self):
        self.adapter = eval(os.getenv('XLSX_ADAPTER'))()
    def fetch_data(self,main_name_list,col_list,fast_track=False,sheet_dict=dict()):
        return self.adapter.sheet_to_dict(main_name_list=main_name_list,col_list=col_list,
                    fast_track=fast_track,sheet_dict=sheet_dict)
