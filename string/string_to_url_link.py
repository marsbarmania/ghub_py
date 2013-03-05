# -*- coding:utf-8 -*-
import re
# using with re module
# format: re.sub(pattern, repl, string, count=0, flags=0)
def convert_to_url_link(str):
  compiled = re.compile("(https?://[a-zA-Z0-9.]{2,}(:[0-9]+)?(/[-_.!~*a-zA-Z0-9;/?:@&=+$,%#]+)?)")
  m = compiled.search(str).group(1)
  return re.sub(compiled,'<a href='+m.encode("utf-8")+'>'+m.encode("utf-8")+'</a>', str)

# text = "Merry X'mas http://www.yahoo.com:3000/aa/bbb?oo=44"
# print convert_to_url_link(text)
