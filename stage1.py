import requests

from env import config

s = requests.Session()
s.headers.update({
    'Authorization': f"Bearer {config['WEBEX_ACCESS_TOKEN']}"
})

WEBEX_BASE_URL = config['WEBEX_BASE_URL']

url = f"{WEBEX_BASE_URL}/v1/rooms"
payload = {
    'title': 'Test'
}
roomId = None
 
response = s.post(url, data=payload)

if response.status_code == 200:
    roomId = response.json()['id']
    with open("env.py", "a") as fo:
        fo.write(f"\nconfig['TESTING_ROOM'] = \"{roomId}\"") 


url2 = f"{WEBEX_BASE_URL}/v1/memberships"
add_to_space = ['mneiding@cisco.com', 'frewagne@cisco.com']

for cec in add_to_space:
    payload = {
        'roomId': roomId,
        'personEmail': cec
        }
    resp = s.post(url2, data=payload)

url3 = f"{WEBEX_BASE_URL}/v1/messages"
payload = {
    'roomId': roomId,
    'text': 'Hi! Sorry this is so late but Im really enjoying the classes :)'.encode('latin-1')
    }
resp = s.post(url3, data=payload)