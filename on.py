import os
import requests

token = os.environ['LIFX_TOKEN']

headers = {
    "Authorization": "Bearer %s" % token,
}



off = {  "power":"on",  "duration": 1,    "fast": "true" }


requests.put('https://api.lifx.com/v1/lights/all/state' , data=off, headers=headers)
