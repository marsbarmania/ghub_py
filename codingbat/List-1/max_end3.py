# -*- coding: utf-8 -*-

# Given an array of ints length 3,
# figure out which is larger between the first
# and last elements in the array,
# and set all the other elements to be that value.
# Return the changed array.

# max_end3([1, 2, 3]) → [3, 3, 3]
# max_end3([11, 5, 9]) → [11, 11, 11]
# max_end3([2, 11, 3]) → [3, 3, 3]

def max_end3(nums):
  repeat_val = nums[0] if nums[0] > nums[2] else nums[2]
  return [repeat_val, repeat_val, repeat_val]


print max_end3([1, 2, 3])
print max_end3([11, 5, 9])
print max_end3([2, 11, 3])
