from urllib2 import urlopen
width = raw_input("image widht")
height = raw_input("image height")
url = 'http://placekitten.com/' + width + '/' + height
kitten = urlopen(url).read()
kitten_file = open("kittens.jpeg","w")
kitten_file.write(kitten)
kitten_file.close()
