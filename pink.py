import os
import requests

token = os.environ['LIFX_TOKEN']


headers = {
    "Authorization": "Bearer %s" % token,
}



green = { "color": "pink",    "brightness": 1,  "power":"on",  "duration": 0.1,    "fast": "false" }
move = { "power_on":"true",  "period": 0 }

requests.put('https://api.lifx.com/v1/lights/all/state' , data=green, headers=headers)
requests.post('https://api.lifx.com/v1/lights/all/effects/move' , data=move, headers=headers)
