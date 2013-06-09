# we've imported urlopen from the urllib2 module,
# which is the Python way of bringing in additional
# functionality we'll need to make our HTTP request.
# A module is just a collection of extra Python tools.
from urllib2 import urlopen

# Open http://placekitten.com/ for reading on line 4!
kittens = urlopen("http://placekitten.com/")
# we'll use urlopen on placekitten.com
# in preparation for our GET request,
# which we make when we read from the site
response = kittens.read()
body = response[559:1000]

# Add your 'print' statement here!
print body
