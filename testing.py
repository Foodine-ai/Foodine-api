import requests
import json

url = 'https://foodineapi.herokuapp.com/foodineapi'

data = {
    'Day':4,
    'Weekend':0,
    'Menu Rating':9.1,
    'Wastage':0
}
j_data = json.dumps(data)
print(j_data)
#headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url,j_data)

print(r)
print(r.json())

