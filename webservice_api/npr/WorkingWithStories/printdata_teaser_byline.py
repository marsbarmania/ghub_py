# This statement will return True
# if variable contains 'key'

# if 'key' in my_dictionary:
from urllib2 import urlopen
from json import load, dumps

url = 'http://api.npr.org/query?apiKey='
key = 'API_KEY'
url = url + key
url += '&numResults=1&format=json&id=1007' #1007 is science
url += '&requiredAssets=image,text,audio'

response = urlopen(url)
json_obj = load(response)

# uncomment 3 lines below to see JSON output to file
#f = open('output.json', 'w')
#f.write(dumps(json_obj, indent=4))
#f.close()

for story in json_obj['list']['story']:
  print "TITLE: " + story['title']['$text'] + "\n"
  print "DATE: " + story['storyDate']['$text'] + "\n"
  print "TEASER: " + story['teaser']['$text'] + "\n"
  if 'byline' in story:
    print "BYLINE: " + story['byline'][0]['name']['$text'] + "\n"
