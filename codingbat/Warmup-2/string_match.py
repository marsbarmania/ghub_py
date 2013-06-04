# -*- coding: utf-8 -*-
# Given 2 strings, a and b, return the number of the positions
# where they contain the same length 2 substring.
# So "xxcaazz" and "xxbaaz" yields 3,
# since the "xx", "aa", and "az" substrings appear in the same place
# in both strings.

# string_match('xxcaazz', 'xxbaaz') → 3
# string_match('abc', 'abc') → 2
# string_match('abc', 'axc') → 0

def string_match(a, b):
  matched = 0
  for i in range(0,len(a)-1):
    # print a[i]+a[i+1]
    search_str = str(a[i]+a[i+1])
    if search_str == str(b[i:i+2]):
      matched += 1
    # if search_str in b:
    #   if b.find(search_str) == i:
    #     matched += 1
  return matched

# print string_match('xxcaazz', 'xxbaaz')
# print string_match('abc', 'abc')
# 1
# print string_match('aabbccdd', 'abbbxxd')
# 3
print string_match('aaxxaaxx', 'iaxxai')

