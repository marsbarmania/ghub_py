# 1.GET: retrieves information from the specified source.
# 2.POST: sends new information to the specified source.
# 3.PUT: updates existing information of the specified source.
# 4.DELETE: removes existing information from the specified source.

# Another way to communicate through HTTP in Python
# is with the requests library
# http://docs.python-requests.org/en/latest/
import requests

# Make a GET request here and assign the result to kittens:
kittens = requests.get("http://placekitten.com/ ")

print kittens.text[559:1000]
