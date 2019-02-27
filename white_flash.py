import os
import requests

token = os.environ['LIFX_TOKEN']


headers = {
    "Authorization": "Bearer %s" % token,
}



data = { "color": "kelvin:9000", "brightness": 1,  "power_on":"true",  "period": 0.1,   "cycles": 5, "persist": "false" }


requests.post('https://api.lifx.com/v1/lights/all/effects/pulse' , data=data, headers=headers)
