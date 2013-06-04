# -*- coding: utf-8 -*-
# Given 3 int values, a b c,
# return their sum.
# However, if any of the values is
# a teen -- in the range 13..19 inclusive
# -- then that value counts as 0,
# except 15 and 16 do not count as a teens.
# Write a separate helper "def fix_teen(n):"that takes
# in an int value and returns that value fixed for the teen rule.
# In this way, you avoid repeating the teen code 3 times
# (i.e. "decomposition").
# Define the helper below and at the same indent level
# as the main no_teen_sum().
def fix_teen(n):
  teens = [13, 14, 17, 18, 19]
  if n in teens: return True
  else:          return False

def no_teen_sum(a, b, c):
  sum = 0

  if not fix_teen(a): sum += a
  if not fix_teen(b): sum += b
  if not fix_teen(c): sum += c

  return sum

print no_teen_sum(1, 2, 3) # 6
print no_teen_sum(2, 13, 1) # 3
print no_teen_sum(2, 1, 14) # 3
