# -*- coding: utf-8 -*-
# Given an array of ints,
# return True if 6 appears as either the first
# or last element in the array.
# The array will be length 1 or more.

# first_last6([1, 2, 6]) → True
# first_last6([6, 1, 2, 3]) → True
# first_last6([13, 6, 1, 2, 3]) → False

def first_last6(nums):
  if nums[0] == 6 or nums[len(nums)-1] == 6: return True
  else: return False
  # try:
  #   six_pos = nums.index(6)
  # except Exception,e:
  #   return False

  # if six_pos == 0 or six_pos == len(nums) - 1:
  #   return True
  # else:
  #   return False
print first_last6([1, 2, 6])
print first_last6([13, 6, 1, 2, 3])
print first_last6([13, 1, 2, 3])
# True
print first_last6([13, 6, 1, 2, 6])
