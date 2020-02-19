import json
import requests

api_key = '579b464db66ec23bdd000001e40dd21c2746437d667c36225001b9cd'
base_url = 'https://api.data.gov.in/resource/794c42c2-8120-4fdc-8773-ec366dd0ac5a'
params = {
    'api-key': api_key,
    'format': 'json',
    'limit': 1,
}
api_url = base_url
response = requests.get(api_url, params=params)

if response.status_code == 200:
    print(response.status_code)

print(response.content)
