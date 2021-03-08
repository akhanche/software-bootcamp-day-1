import requests
from requests.auth import HTTPBasicAuth

from env import config

headers = {
    "X-Cisco-Meraki-API-Key": config['MERAKI_KEY']
}

orgs_url = f"{config['MERAKI_BASE_URL']}/organizations"
resp = requests.get(orgs_url, headers=headers)


if resp.status_code == 200:
    print("Meraki Access verified")
else:
    print(f"Meraki status code: {resp.status_code}")



#url = "https://api.meraki.com/api/v0/organizations"

payload = None

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": config['MERAKI_KEY']
}

response = requests.request('GET', orgs_url, headers=headers, data = payload).json()

#print(response.text.encode('utf8'))

for org in response:
    print("orgId:" + org["id"], "name:" + org["name"])    
