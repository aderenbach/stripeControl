import os
import requests

token = os.environ['LIFX_TOKEN']

headers = {
    "Authorization": "Bearer %s" % token,
}



pink = { "color": "pink",    "brightness": 1,  "power":"on",  "duration": 0,    "fast": "true" }
white = { "color": "kelvin:9000",    "brightness": 0.6,  "power":"on",  "duration": 0,    "fast": "true" }
move = { "power_on":"true",  "period": 1 }

requests.put('https://api.lifx.com/v1/lights/all/state' , data=pink, headers=headers)
requests.put('https://api.lifx.com/v1/lights/all|0|2|4|6|8|10|12|14/state' , data=white, headers=headers)
requests.post('https://api.lifx.com/v1/lights/all/effects/move' , data=move, headers=headers)
