import json
import requests
payload={'season': 2020, 'sort': 'asc'}
result = requests.get('https://api-football-standings.azharimm.site/leagues/eng.1/standings', params=payload)
res=result.json()
res=json.loads(result.text)
# print(res)
# print(json.dumps(res, indent=4))
with open('data.json','w')as file:
    json.dump(res,file, indent=4)

print("გუნდის დასახელება: ", res['data']['standings'][0]['team']['name'])
print("გუნდის აბრივიატურა: ", res['data']['standings'][0]['team']['abbreviation'])
print("გუნდის მიერ გატანილი გოლების რაოდენობა: ",res['data']['standings'][0]['stats'][4]['value'])
print("გუნდის მიერ გაშვებული გოლების რაოდენობა: ", res['data']['standings'][0]['stats'][5]['value'])

# print(result.text)
# print(result.status_code)
# print(result.headers)