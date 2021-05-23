import requests
import json
BASE = "http://127.0.0.1:5000/"
main_name_list = ['Ingram','Scansource','Comstor']
fast_col_list = ['Cisco Standard Part Number',"Distributor Part Number",'Available']
new_response = requests.put(BASE +"update")
response = requests.get(BASE+"tables/"+str(main_name_list)+"/"+str(fast_col_list))
thing = response.json()
print(thing['data']['Ingram'])
#new_response = requests.put(BASE +"update")
#print(new_response.json())
#print(new_response)