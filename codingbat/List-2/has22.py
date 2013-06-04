# -*- coding: utf-8 -*-
# Given an array of ints,
# return True
# if the array contains a 2 next to a 2 somewhere.
def has22(nums):
  if len(nums) == 0: return False
  if 2 in nums:
    ans = False
    index = 0
    while index < len(nums)-1:
      if nums[index]==2 and nums[index+1]==2: ans = True
      index += 1
    return ans
  else:
    return False

# print has22([1, 2, 2]) # True
# print has22([1, 2, 1, 2]) # False
# print has22([2, 1, 2]) # False

# print has22([2, 2, 1, 2]) # True
# print has22([1, 3, 2]) # False
# print has22([1, 3, 2, 2]) # True
# print has22([2, 3, 2, 2]) # True  False X
# print has22([4, 2, 4, 2, 2, 5]) # True  False X
# print has22([1, 2]) # False
# print has22([2, 2]) # True
# print has22([2]) # False
# print has22([]) # False
# print has22([3, 3, 2, 2]) # True
print has22([5, 2, 5, 2]) # False
