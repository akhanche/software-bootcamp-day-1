# ACME Corp. wants you to show them Umbrellas capabilites on some URLs.
# The SOC team leader Dominik asks you to use Umbrellas API capabilities 
# to get the domain status and all historical information about an URL that is 
# available in Umbrella. Once you gathered this information it should be printed 
# out in a readable, report-like format with sanitized URLs.

# Any URL that is returned as malicious should be added to a block list through the Umbrella API.
#  He would like you to do that for any URL that would be inserted by the team in any fashion.

# For test purposes you can use internetbadguys(dot)com.

import requests
import json
import sys
from pathlib import Path
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from pprint import pprint

here = Path(__file__).parent.absolute()
repository_root = (here / ".." ).resolve()
sys.path.insert(0, str(repository_root))

import env

inv_url = env.UMBRELLA.get("inv_url")
inv_token = env.UMBRELLA.get("inv_token")
domain = "internetbadguys.com"