# -*- coding: utf-8 -*-
# Return the number of times
# that the string "hi" appears anywhere in the given string.
def count_hi(str):
  return len(str.split("hi")) - 1

print count_hi('abc hi ho') # 1
print count_hi('ABChi hi') # 2
print count_hi('hihi') # 2

# Solution:

# def count_hi(str):
#   sum = 0
#   ## Loop to length-1 and access index i and i+1
#   ## in the loop.
#   for i in range(len(str)-1):
#     if str[i:i+2] == 'hi':
#       sum = sum + 1
#   return sum
