import os
import requests

token = os.environ['LIFX_TOKEN']
stripeId = os.environ['LIFX_STRIPID']


headers = {
    "Authorization": "Bearer %s" % token,
}



black = { "color": "white",    "brightness": 0,  "power":"on",  "duration": 0,    "fast": "false" }
white = { "color": "blue",    "brightness": 1,  "power":"on",  "duration": 0,    "fast": "false" }
move = { "power_on":"true",  "period": 0.5 ,    "fast": "false" }

requests.post('https://api.lifx.com/v1/lights/id:'+stripeId+'/effects/move' , data=move, headers=headers)
requests.put('https://api.lifx.com/v1/lights/id:'+stripeId+'|0-15/state' , data=black, headers=headers)
requests.put('https://api.lifx.com/v1/lights/id:'+stripeId+'|0|6/state' , data=white, headers=headers)

