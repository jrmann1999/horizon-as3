#! python

import requests
import json
from requests.auth import HTTPBasicAuth

url = "https://BIGIP:8443/mgmt/shared/appsvcs/declare"

with open('app.json') as file:
    json_data = json.load(file)

r = requests.post(url, data=json.dumps(json_data), auth=HTTPBasicAuth('USER', 'PASS'), verify=False)

print (r.content)