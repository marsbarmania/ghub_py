from urllib2 import urlopen
url = 'http://placekitten.com/200/300'
kitten = urlopen(url).read()
kitten_file = open("kittens.jpeg","w")
kitten_file.write(kitten)
kitten_file.close()
