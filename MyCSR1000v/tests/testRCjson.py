import requests , json, urllib3


requests.packages.urllib3.disable_warnings()

#Connection address
url = "https://192.168.56.101/restconf"

#Headers
headers = {'Accept': 'application/yang-data+json','Content-Type': 'application/yang-data+json'}

#Authentication

username="lucemilian"
password="devnet2020!"
basic_auth      =(username,password)
resp = requests.get(url, auth=basic_auth,headers=headers, verify=False)
print("Request status", resp.status_code)


rJSON=resp.json()
print("Router's yang version is:",rJSON["restconf"]["yang-library-version"])