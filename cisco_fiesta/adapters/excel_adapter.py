import pandas as pd

class XlsReader():
    def __init__(self,file_path='./data/input_file.xlsx'):
        self.xls = pd.ExcelFile(file_path)
    def get_main_sheet(self,sheet_name,col_list=[]):
            self.sheet = pd.read_excel(self.xls,sheet_name)
            self.sheet = self.sheet[self.sheet['Cisco Standard Part Number'].notna()]
            self.columns = col_list
            self.sheet = XlsReader.error_handle_cols(self,self.columns)
            return self.sheet.fillna(0)       
    def get_ft_sheet(self,sheet_name,col_list):
        self.sheet = pd.read_excel(self.xls,sheet_name)
        self.sheet = self.sheet[self.sheet['FT Part Number'].notna()]
        self.columns = col_list
        self.sheet,self.columns = XlsReader.error_handle_cols(self,self.columns,fast_track=True)
        return self.sheet.fillna(0)
    def sheet_to_dict(self,main_name_list=[],col_list=[],fast_track=False,sheet_dict = dict()):
        #this sould be re-made into a more efficient func
        self.sheet_name_list = main_name_list
        self.df_list = []
        self.sheet_dict = sheet_dict
        if fast_track==False:
            for item in main_name_list:
                self.df_list.append(XlsReader.get_main_sheet(self,sheet_name=item,col_list=col_list))
                for _item in self.df_list:
                    self.sheet_dict[item] = _item.to_json()
            return  self.sheet_dict
        if fast_track == True:
            for item in main_name_list:
                self.df_list.append(XlsReader.get_ft_sheet(self,sheet_name=item,col_list=col_list))
                for _item in self.df_list:
                    self.sheet_dict[item] = _item.to_json()
            return  self.sheet_dict
    def error_handle_cols(self,col_list,fast_track=False):
        self.col_list = col_list
        try:
            self.sheet = self.sheet[self.col_list]
            
        except:
            try:
                self.col_list[-1] = 'Avaiable'
                self.sheet = self.sheet[self.col_list]
            except:
                raise KeyError('Please check if the column names in the excel file/sheet are: {}'.format(self.col_list))
        if fast_track==False:
            return self.sheet
        else:
            return self.sheet,self.columns
class FakeXlsReader:
    def __init__(self,file_path='./data/input_file.xlsx'):
        pass
    def get_main_sheet(self,sheet_name,col_list=[]):
        pass
    def get_ft_sheet(self,sheet_name,col_list):
        pass
    def sheet_to_dict(self,main_name_list=[],col_list=[],fast_track=False,sheet_dict = dict()):
        pass
    def error_handle_cols(self,col_list,fast_track=False):
        pass