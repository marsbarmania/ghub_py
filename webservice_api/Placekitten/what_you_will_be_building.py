from urllib2 import urlopen

width = raw_input("How wide do you want your image to be?")
height = raw_input("How tall do you want your image to be?")

url = 'http://placekitten.com/' + width + '/' + height
kitten = urlopen(url).read()

f = open('kittens.jpeg', 'w')
f.write(kitten)
f.close()
