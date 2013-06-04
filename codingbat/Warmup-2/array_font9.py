# -*- coding: utf-8 -*-

# Given an array of ints,
# return True if one of the first 4 elements in the array is a 9.
# The array length may be less than 4.

# array_front9([1, 2, 9, 3, 4]) → True
# array_front9([1, 2, 3, 4, 9]) → False
# array_front9([1, 2, 3, 4, 5]) → False

def array_front9(nums):
  ans = False
  loop = 4 if len(nums) >= 4 else len(nums)
  for i in range(0,loop):
    if nums[i] == 9: ans = True
  return ans

print array_front9([1, 2, 9, 3, 4])
print array_front9([1, 2, 3, 4, 9])
print array_front9([1, 2, 3])
