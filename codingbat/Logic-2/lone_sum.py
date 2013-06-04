# -*- coding: utf-8 -*-
# Given 3 int values, a b c,
# return their sum. However,
# if one of the values is the same as another of the values,
# it does not count towards the sum.

# def lone_sum(a, b, c):
#   if a != b and a != c and a != b and b != c:
#     return a + b + c
#   elif a != b and a != c and b == c:
#     return a
#   elif a != b and a == c and b != c:
#     return b
#   elif a == b and a != c and b != c:
#     return c
#   else:
#     return 0

def lone_sum(a, b, c):
  sum = 0
  if a != b and a != c: sum += a
  if b != a and b != c: sum += b
  if c != a and c != b: sum += c
  return sum





print lone_sum(1, 2, 3) # 6
print lone_sum(3, 2, 3) # 2
print lone_sum(3, 3, 3) # 0
print lone_sum(9, 2, 2) # 9
print lone_sum(2, 2, 9) # 9
