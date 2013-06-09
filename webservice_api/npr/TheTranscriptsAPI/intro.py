from urllib2 import urlopen
from json import load, dumps

#transcript API call URL
url = 'http://api.npr.org/transcript?apiKey=API_KEY'
url += '&format=json&id=152248901'

response = urlopen(url)
j = load(response)

#print transcript paragraphs
for paragraph in j["paragraph"]:
  print paragraph["$text"] + "\n"

# uncomment 3 lines below to see JSON output to file
#f = open('output.json', 'w')
#f.write(dumps(j, indent=4))
#f.close()
