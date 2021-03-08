import requests
import json
from env import config

# Get organisation list from meraki sandbox


url = f"{config['MERAKI_BASE_URL']}/organizations/{config['MERAKI_ORG_ID']}/devices"

#devices = []
#for device in resp:
payload = None

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": config['MERAKI_KEY']
}

response = requests.get(url, headers=headers, data=payload).json()

devices = {}
devices['devices'] = []
for device in response:
    devices['devices'].append({
        'name': device['name'],
        'mac': device['mac'],
        'serial': device['serial'],
        'type': device['model']
    })

print(devices)

#print(response.text.encode('utf8'))


#f = open('devicelist.json', 'w')
#f.write()
#f.close()
with open('devicelist.json', 'w') as outfile:
    json.dump(devices, outfile, indent=4)