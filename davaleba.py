import json

import requests

key= 'WjINODGkH4GcOUoCWrEfTawclVU0y2uYiM8LIsVXVefiUAxOt33RYgXWc27f'
payload={'api_token':'WjINODGkH4GcOUoCWrEfTawclVU0y2uYiM8LIsVXVefiUAxOt33RYgXWc27f', 'include':'country' }
r=requests.get('https://soccer.sportmonks.com/api/v2.0/leagues/271', params=payload)

# print(r.text)

res= json.loads(r.text)

print(res)
print(json.dumps(res, indent=4))