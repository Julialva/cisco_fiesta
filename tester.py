import requests
BASE = "http://127.0.0.1:5000/"
ft_name_list = ['Ingram Fast Track','Scansource Fast Track','Comstor Fast Track']
fast_col_list = ['FT Part Number','Avaiable']
response = requests.get(BASE+"fastables/"+str(ft_name_list)+"/"+str(fast_col_list))
print(response.json())