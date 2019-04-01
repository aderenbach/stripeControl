import os
import requests

token = os.environ['LIFX_TOKEN']


headers = {
    "Authorization": "Bearer %s" % token,
}



red = { "color": "red",    "brightness": 1,  "power":"on",  "duration": 0.1,    "fast": "false" }

move = { "power_on":"true",  "period": 0 ,    "fast": "false" }

requests.put('https://api.lifx.com/v1/lights/all/state' , data=red, headers=headers)
requests.post('https://api.lifx.com/v1/lights/all/effects/move' , data=move, headers=headers)
