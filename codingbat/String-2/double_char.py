# -*- coding: utf-8 -*-
# Given a string, return a string where
# for every char in the original, there are two chars.

def double_char(str):
  new_str = ""
  for s in str:
    new_str += s*2
  return new_str

print double_char('The') # 'TThhee'
print double_char('AAbb') # 'AAAAbbbb'
print double_char('Hi-There') # 'HHii--TThheerree'

# Solution:

# def double_char(str):
#   result = ""
#   for i in range(len(str)):
#     result += str[i] + str[i]
#   return result
