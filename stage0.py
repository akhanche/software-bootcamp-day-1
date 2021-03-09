from env import config
import requests
url = "https://webexapis.com/v1/rooms"
headers = {'Authorization': f"Bearer {config['WEBEX_ACCESS_TOKEN']}"}
response = requests.get(url, headers=headers).json()

for i in response['items']:
    if i['title'] == 'CSAP Programmability CTF - Team 2':
        print("Room ID is :" ,i['id'])