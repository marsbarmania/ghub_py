# -*- coding: utf-8 -*-

# Given a non-empty string like "Code"
# return a string like "CCoCodCode".

# string_splosion('Code') → 'CCoCodCode'
# string_splosion('abc') → 'aababc'
# string_splosion('ab') → 'aab'

def string_splosion(str):
  range_end = 1
  new_str = ""
  for i in range(0,len(str)):
    new_str += str[0:range_end]
    range_end += 1
  return new_str

print string_splosion('abc')
