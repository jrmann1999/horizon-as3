#!/usr/bin/env python
import requests
import base64
import json

IP = "BIGIP"
PORT = "8443"
CREDS = "USER:PASS"

encodedCREDS = str(base64.b64encode(CREDS.encode("utf-8")), "utf-8")

h = {'Host': 'localhost', 'Authorization': 'Basic ' + encodedCREDS, 'Content-Type': 'application/json'}
authd = {"username": "USER", "password": "PASS", "loginProviderName": "tmos"}

with open('app-validate.json', 'w') as file:
    t = requests.get(
        "https://" + IP + ":" + PORT + "/mgmt/shared/appsvcs/declare", 
        headers=h, 
        verify=False
    )
    print(t.status_code)
    print(t.json())
    file.writelines(json.dumps(t.json(), indent='\t'))