import pandas as pd

class xls_reader():
    def __init__(self,file_path=''):
        self.xls = pd.ExcelFile(file_path)
    def get_main_sheet(self,sheet_name):
            self.sheet = pd.read_excel(self.xls,sheet_name)
            self.sheet = self.sheet[self.sheet['Cisco Standard Part Number'].notna()]
            try:
                self.sheet = self.sheet[['Cisco Standard Part Number','Distributor Part Number','Product Item Description',
                            'Quantity on Hand','Quantity On Order','Distributor Reported In-transit Quantity','Committed Quantity','Available']]
            except:
                self.sheet = self.sheet[['Cisco Standard Part Number','Distributor Part Number','Product Item Description',
                            'Quantity on Hand','Quantity On Order','Distributor Reported In-transit Quantity','Committed Quantity','Avaiable']]
            return self.sheet
    def sheet_to_dict(self,sheet_name_list=[]):
        self.sheet_name_list = sheet_name_list
        self.df_list = []
        self.sheet_dict = dict()
        for item in sheet_name_list:
            self.df_list.append(xls_reader.get_main_sheet(self,sheet_name=item))
            for _item in self.df_list:
                self.sheet_dict[item] = _item
        return  self.sheet_dict
            


xls = xls_reader(file_path='/Users/julialva/Desktop/cisco_fiesta/cisco_fiesta/input_files/17_05_2021_Situação Atual Inventário Distribuição.xlsx')
sheet_name_list = ['Ingram','Scansource','Comstor']
dicto = xls_reader.sheet_to_dict(xls,sheet_name_list=sheet_name_list)
print(dicto)