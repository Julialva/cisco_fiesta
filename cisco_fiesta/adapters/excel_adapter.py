import pandas as pd

class XlsReader():
    def __init__(self,file_path='./data/input_file.xlsx'):
        self.xls = pd.ExcelFile(file_path)
    def get_main_sheet(self,sheet_name,col_list=[]):
            self.sheet = pd.read_excel(self.xls,sheet_name)
            self.sheet = self.sheet[self.sheet['Cisco Standard Part Number'].notna()]
            self.columns = col_list
            return XlsReader.error_handle_cols(self,self.columns)
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
    def standard_procedure(self):
        #needs to be changed? don't know how to make it better yet ;-;
        main_name_list = ['Ingram','Scansource','Comstor']
        ft_name_list = ['Ingram Fast Track','Scansource Fast Track','Comstor Fast Track']
        col_list = ['Cisco Standard Part Number','Distributor Part Number','Product Item Description',
                            'Quantity on Hand','Quantity On Order','Distributor Reported In-transit Quantity','Committed Quantity','Available']
        fast_col_list = ['FT Part Number','Avaiable']
        dicto = XlsReader.sheet_to_dict(self,main_name_list=main_name_list,col_list=col_list)
        final_dicto = XlsReader.sheet_to_dict(self,main_name_list=ft_name_list,col_list=fast_col_list,fast_track=True,sheet_dict = dicto)
        return final_dicto
class FakeXlsReader:
    def __init__(self,file_path=0):
        pass
    def standard_procedure():
        pass


