import os
import requests

token = os.environ['LIFX_TOKEN']
stripeId = os.environ['LIFX_STRIPID']


headers = {
    "Authorization": "Bearer %s" % token,
}



move = { "power_on":"true",  "period": 3 }

requests.post('https://api.lifx.com/v1/lights/id:'+stripeId+'/effects/move' , data=move, headers=headers)

