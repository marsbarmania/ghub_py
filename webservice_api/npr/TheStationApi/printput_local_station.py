from urllib2 import urlopen
from json import load

key = "API_KEY"

def build_api_call(key):
  url = "http://api.npr.org/stations"
  url += "?apiKey=" + key
  url += "&format=json"
  zip_code = raw_input("Enter your zip code:")
  url += "&zip=" + zip_code
  return url

def call_station_api(url):
  response = urlopen(url)
  j = load(response)
  return j

def parse_station_json(json_obj):
  for station in json_obj['station']:
    print station['callLetters']['$text']+"\n"
    print ": "
    print station['marketCity']['$text']+"\n"
    print ", "
    print station['state']['$text'] + "\n"
url = build_api_call(key)
print "URL :" + url

json_obj = call_station_api(url)
parse_station_json(json_obj)
