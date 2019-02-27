
import requests

token = ""

headers = {
    "Authorization": "Bearer %s" % token,
}

k3000 = { "color": "kelvin:9000",    "brightness": 1,  "power":"on",  "duration": 0,    "fast": "false" }
k9000 = { "color": "red",    "brightness": 1,    "duration": 0,    "fast": "false" }

#requests.put('https://api.lifx.com/v1/lights/all/state'    , data=k3000, headers=headers)
requests.put('https://api.lifx.com/v1/lights/all/state' , data=k9300, headers=headers)
#requests.put('https://api.lifx.com/v1/lights/all|1-3/state'    , data=k3000, headers=headers)

#response = requests.post('https://api.lifx.com/v1/lights/all/effects/move', data={     "period": 2,     "direction": "backward"}, headers=headers)