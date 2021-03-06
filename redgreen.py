import os
import requests

token = os.environ['LIFX_TOKEN']


headers = {
    "Authorization": "Bearer %s" % token,
}



black = { "color": "white",    "brightness": 0,  "power":"on",  "duration": 0,    "fast": "false" }
blue = { "color": "green",    "brightness": 1,  "power":"on",  "duration": 0,    "fast": "false" }
red = { "color": "red",    "brightness": 1,  "power":"on",  "duration": 0,    "fast": "false" }
move = { "power_on":"true",  "period": 1 ,    "fast": "false" }

requests.post('https://api.lifx.com/v1/lights/all/effects/move' , data=move, headers=headers)
requests.put('https://api.lifx.com/v1/lights/all|0-15/state' , data=black, headers=headers)
requests.put('https://api.lifx.com/v1/lights/all|0-2/state' , data=blue, headers=headers)
requests.put('https://api.lifx.com/v1/lights/all|8-10/state' , data=red, headers=headers)

