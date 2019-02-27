import os
import requests

token = os.environ['LIFX_TOKEN']


headers = {
    "Authorization": "Bearer %s" % token,
}



black = { "color": "white",    "brightness": 0,  "power":"on",  "duration": 0,    "fast": "true" }
white = { "color": "white",    "brightness": 1,  "power":"on",  "duration": 0,    "fast": "true" }
move = { "power_on":"true",  "period": 1 }

requests.post('https://api.lifx.com/v1/lights/all/effects/move' , data=move, headers=headers)
requests.put('https://api.lifx.com/v1/lights/all|0-15/state' , data=black, headers=headers)
requests.put('https://api.lifx.com/v1/lights/all|0/state' , data=white, headers=headers)

