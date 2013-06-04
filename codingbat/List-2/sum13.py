# -*- coding: utf-8 -*-
# Return the sum of the numbers in the array,
# returning 0 for an empty array.
# Except the number 13 is very unlucky,
# so it does not count and numbers
# that come immediately after a 13 also do not count.
def sum13(nums):
  if len(nums) == 0: return 0
  sum = 0
  for index,val in enumerate(nums):
    if val != 13:
      sum += val
    else:
      if index != len(nums)-1:
        nums[index + 1] = 0
  return sum



# print sum13([1, 2, 2, 1]) # 6
# print sum13([1, 1]) # 2
# print sum13([1, 2, 2, 1, 13]) # 6

print sum13([1, 2, 13, 2, 1, 13]) # 4
print sum13([13, 1, 2, 13, 2, 1, 13]) # 3
print sum13([13, 1, 13]) # 0
print sum13([5, 13, 2]) # 5
