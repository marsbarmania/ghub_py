# -*- coding: utf-8 -*-
# Given a string, return a new string where the first
# and last chars have been exchanged.

# front_back('code') → 'eodc'
# front_back('a') → 'a'
# front_back('ab') → 'ba'

def front_back(str):
  if len(str) == 1 or len(str) == 0: return str
  if len(str) == 2: return str[::-1]

  new_char = ""
  new_char += str[len(str) - 1]
  new_char += str[1:len(str)-1]
  new_char += str[0]
  return new_char

print front_back('code')
