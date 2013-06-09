from urllib2 import urlopen
from json import load

key = "API_KEY"
url = "http://api.npr.org/transcript?apiKey=" + key
url += '&format=json&id=152248901'
response = urlopen(url)
j = load(response)
for paragraph in j['paragraph']:
  print paragraph["$text"] + "\n"
