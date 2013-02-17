# coding:UTF-8
import sys
inp = open('text.txt','r')
str_raw = inp.read()
str_num = (ord(str) for str in str_raw)
str_con = "".join([chr(str^255) for str in str_num])
inp.close()

f = open('text_encoded.txt', 'w')

f.write(str_con)
f.close()