import sys
import requests
import json

newName = sys.argv[3]
deviceID = sys.argv[2]

def rename(key):
    headers = {'authorization': "basic "  + key}
    
    r = requests.post("https://api.bymason.com/v1/default/device/" + deviceID, headers=headers, json={"name": newName})     


def callMason(key):
    headers = {'authorization': "basic "  + key}
    r = requests.get("https://api.bymason.com/v1/default/device/" + deviceID, headers=headers)
    j = r.json()
    

    for x in j["data"]:
        print("New Name: " + x["name"])
    



if len(sys.argv) < 3:
    print("Please include an APIKey, device ID, and a new device name.")
else:
    rename(sys.argv[1])
    callMason(sys.argv[1])
    