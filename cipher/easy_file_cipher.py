# coding:UTF-8

with open("text.txt","r") as origin_file:
  stream_raw = origin_file.read()
  # ord(): the codepoint of the string
  str_num = (ord(str) for str in stream_raw)
  seed = 255
  # str_con = "".join([chr(str^seed) for str in str_num])
  str_con = "".join(map(lambda str: chr(str^seed),str_num))

  with open('text_encode.txt', 'w') as new_file:
    new_file.write(str_con)
