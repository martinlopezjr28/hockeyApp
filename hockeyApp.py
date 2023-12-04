import requests as req
import json as j

api_endpoint="https://api-web.nhle.com/v1/player/8478445/landing"

response = req.get(api_endpoint)

if response.status_code == 200:
    print(j.dumps(response.json(), indent=4))
else:
    print(f'Error: {response.status_code}')
    response.text