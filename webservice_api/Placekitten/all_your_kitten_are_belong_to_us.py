from urllib2 import urlopen
# url = str('http://placekitten.com/200/300')
url = u'http://placekitten.com/200/300'.encode('utf-8')
kitten = urlopen(url).read()
