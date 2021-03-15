#!/usr/bin/env python

import requests
import json
import sys
from pathlib import Path
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from pprint import pprint
from datetime import datetime
from time import time

here = Path(__file__).parent.absolute()
repository_root = (here / ".." ).resolve()
sys.path.insert(0, str(repository_root))

import env

inv_url = env.UMBRELLA.get("inv_url")
inv_token = env.UMBRELLA.get("inv_token")
domain = "internetbadguys.com"
en_url = env.UMBRELLA.get("en_url")
en_key = env.UMBRELLA.get("en_key")

# url = f"{inv_url}/domains/categorization/{domain}?showLabels"
# headers = {"Authorization": f'Bearer {inv_token}'}
# response = requests.get(url, headers=headers)

# response.raise_for_status()
# domain_status = response.json()[domain]["status"]
# print("\n")
# if domain_status == 1:
#     print(f"The domain {domain} is found CLEAN")
# elif domain_status == -1:
#     print(f"The domain {domain} is found MALICIOUS")
# elif domain_status == 0:
#     print(f"The domain {domain} is found UNDEFINED")

# print("This is how the response data from Umbrella Investigate looks like: \n")
# pprint(response.json(), indent=4)

#Add another call here, where you check the historical data for either the domain from the intro or your own domain and print it out in a readable format
#url = f"{inv_url}/pdns/domain/{domain}"
#querystring = {"sortorder":"desc"}
#headers = {
#    "Accept": "application/json",
#    "Authorization": f'Bearer {inv_token}'}
#response = requests.get(url, headers=headers, params=querystring)
#response.raise_for_status()

####################################
#Stage 1
#current_time = datetime.utcfromtimestamp(time()).strftime("%Y-%m-%dT%H:%m:%SZ")

#payload = {"alertTime": f"{current_time}",
#                    "deviceId": "ba6a59f4-e692-4724-ba36-c28132c761de",
#                    "deviceVersion": "13.7a",
#                    "dstDomain": f"{domain}",
#                    "dstUrl": f"{domain}",
#                    "eventTime": f"{current_time}",
#                    "protocolVersion": "1.0a",
#                    "providerName": "Security Platform"}
#payload = json.dumps(payload)
#headers2 = {"Content-Type": "application/json"}

#response2 = requests.post(f"{en_url}events?customerKey={en_key}", headers = headers2, data = payload)
#print(response2)

def getDomainStatus(domain):
    #Construct the API request to the Umbrella Investigate API to query for the status of the domain
    url = f"{inv_url}/domains/categorization/{domain}?showLabels"
    headers = {"Authorization": f'Bearer {inv_token}'}
    response = requests.get(url, headers=headers)

    #And don't forget to check for errors that may have occured!
    response.raise_for_status()
    #Make sure the right data in the correct format is chosen, you can use print statements to debug your code
    domain_status = response.json()[domain]["status"]

    if domain_status == 1:
        print(f"The domain {domain} is found CLEAN")
    elif domain_status == -1:
        print(f"The domain {domain} is found MALICIOUS")
    elif domain_status == 0:
        print(f"The domain {domain} is found UNDEFINED")

    print("This is how the response data from Umbrella Investigate looks like: \n")
    pprint(response.json(), indent=4)

    return domain_status


def getDomainHistory(domain):
    url = f"{inv_url}/whois/{domain}/history"

    headers = {"Accept": "application/json",
    "Authorization": f'Bearer {inv_token}'}
    response = requests.request("GET", url, headers=headers)
    data = response.json()
    pprint(response.json(), indent=4)

    return data

def addToBlockList(domain):
    url = f"{en_url}/events?customerKey={en_key}"
    
    headers = {"Content-Type": "application/json"}
    data= {"alertTime": "2021-03-11T18:20:36.284Z",
    "deviceId": "AbdullahTest",
    "deviceVersion": "13.7a",
    "dstDomain": f"{domain}",
    "dstUrl": f"{domain}",
    "eventTime": "2021-03-11T18:20:36.284Z",
    "protocolVersion": "1.0a",
    "providerName": "Security Platform"}

    response = requests.request("POST", url, headers=headers, data=json.dumps(data))

    data = response.json()
    pprint(response.json(), indent=4)

    return data

def getBlockList():
    url = f"{en_url}/domains?customerKey={en_key}"

    headers = {"Accept": "application/json"}

    response = requests.request("GET", url, headers=headers)
    data = response.json()
    pprint(response.json(), indent=4)

    return data

def main ():

    request1 = getDomainStatus(domain)
    request2 = getDomainHistory(domain)
    #if the domain is malicious we add it to the block list
    if request1 == -1: 
        request3 = addToBlockList(domain)
    request4 = getBlockList()

if __name__ == "__main__":
    main()    