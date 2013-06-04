# -*- coding: utf-8 -*-
# Given a number n,
# return True if n is in the range 1..10, inclusive.
# Unless "outsideMode" is True,
# in which case return True if the number is less or equal to 1,
# or greater or equal to 10.

def in1to10(n, outside_mode):
  if outside_mode:
    return True if n <= 1 or n >= 10 else False
  else:
    return True if 1 <= n <= 10 else False

print in1to10(5, False) # True
print in1to10(11, False) # False
print in1to10(11, True) # True
