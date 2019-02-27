import os
import requests

token = os.environ['LIFX_TOKEN']

headers = {
    "Authorization": "Bearer %s" % token,
}



move = { "power_on":"true",  "period": 0.5 }

requests.post('https://api.lifx.com/v1/lights/all/effects/move' , data=move, headers=headers)

