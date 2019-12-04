import sys
import requests
import json

def callMason(key):
    headers = {'authorization': "basic "  + key}
    r = requests.get("https://api.staging.masonamerica.net/v1/default/device", headers=headers)
    j = r.json()

    for x in j["data"]:
        print("DeviceID: " + x["id"] + ", lastcheckin " + x["lastcheckin"])

if len(sys.argv) < 2:
    print("Please include an APIKey")
else:
    callMason(sys.argv[1])