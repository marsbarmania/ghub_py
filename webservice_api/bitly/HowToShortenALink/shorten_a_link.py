import requests
import json

query_params = {'access_token': 'API_KEY',
                'longUrl': 'http://blog.marsbar.us/blog/2013/02/23/evernoteapi-basic/'}

endpoint = 'https://api-ssl.bitly.com/v3/shorten'
response = requests.get(endpoint, params= query_params)

data = json.loads(response.content)
print data
