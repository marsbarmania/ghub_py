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
    print "Frequency: "
    print station['frequency']['$text']+'\n'
    print station['band']['$text']+'\n'
    if 'url' in station:
      print "MP3 Streams: "
      for link in station['url']:
        if link['type'] == "Audio MP3 Stream":
          print "\t" + link["title"] + "-" + link["$text"]
    print station['callLetters']['$text']+"\n"
    print ": "
    print station['marketCity']['$text']+"\n"
    print ", "
    print station['state']['$text'] + "\n"
url = build_api_call(key)
print "URL :" + url

json_obj = call_station_api(url)
parse_station_json(json_obj)
