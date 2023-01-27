import requests
import json
params = {
   'amount' : 10,
    'type'  : 'boolean'
}


response = requests.get('https://opentdb.com/api.php',params=params)
response.raise_for_status
# x = response.json() # alternate

x = json.loads(response.text)

question_data = x.get('results')