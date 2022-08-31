import json
import requests

url = 'http://localhost:8000'

client_name = 'test' ## Onesemi1, Onesemi2, Onesemi3
lib_name = 'Runfile_template' ## Same name with Runfile.py
method_idx = 0 ## Choose one method below

'''
    method_idx = 0 : _CalculateDesignParameter1
    method_idx = 1 : _CalculateDesignParameter2
'''

args_dict = dict(
vss2nmos=None,
vdd2pmos=None,
sd_width=66,
gate_spacing=110,
vdd2vss_height=1800,
nmos_width=200,
pmos_width=400,
length=40,
nmos_gate=1,
pmos_gate=1,
XVT='RVT') ## Write the input parameters of generator source code

print (args_dict)
json_input_data = dict(client_name = client_name, lib_name = lib_name, method_idx = method_idx, args_str = str(json.dumps(args_dict)))
print(requests.post(url=url, data=json.dumps(json_input_data)).text)