# Try entering a few different NPR ID's:
# 1001 : News topic
# 1002 : NPR.org homepage feed
# 1045 : Movies topic
# 1007 : Science topic
# 1032 : Economy topic
# 1039 : NPR Music
# 2 : 'All Things Considered` program
# 5500502 : 'Krulwich Wonders...' blog
# 2101154 : stories by Ari Shapiro
# 93568166 : 'Monkey See' Pop Culture

from urllib2 import urlopen
from json import load

npr_id = raw_input("Which NPR ID do you want to query?")

url = "http://api.npr.org/query?apiKey="
key = "API_KEY"
url += key
url += "&numResults=3&format=json&id="
url += npr_id

response = urlopen(url)
json_obj = load(response)
for story in json_obj['list']['story']:
  print story['title']['$text']
