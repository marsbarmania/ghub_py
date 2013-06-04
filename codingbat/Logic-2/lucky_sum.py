# -*- coding: utf-8 -*-
# Given 3 int values, a b c, return their sum.
# However,
# if one of the values is 13 then it does not count towards the sum
# and values to its right do not count.
# So for example, if b is 13, then both b and c do not count.

def lucky_sum(a, b, c):
  total = 0
  if a != 13:
    total += a
    if b != 13:
      total += b
      if c != 13:
        total += c
  return total



print lucky_sum(1, 2, 3) # 6
print lucky_sum(1, 2, 13) # 3
print lucky_sum(1, 13, 3) # 1
