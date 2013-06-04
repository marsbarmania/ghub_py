# -*- coding: utf-8 -*-
# Given an array length 1 or more of ints,
# return the difference between the largest
# and smallest values in the array.
# Note: the built-in min(v1, v2) and max(v1, v2)
# functions return the smaller or larger of two values.

def big_diff(nums):
  big = 0
  small = 0
  for index,num in enumerate(nums):
    if index == 0:
      big = num
      small = num
    else:
      big = max(big,num)
      small = min(small,num)

  return big - small

print big_diff([10, 3, 5, 6]) # 7
print big_diff([7, 2, 10, 9]) # 8
print big_diff([2, 10, 7, 2]) # 8
