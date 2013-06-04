# -*- coding: utf-8 -*-
# Given an array of ints,
# return True if .. 1, 2, 3, .. appears in the array somewhere.

# array123([1, 1, 2, 3, 1]) → True
# array123([1, 1, 2, 4, 1]) → False
# array123([1, 1, 2, 1, 2, 3]) → True

def array123(nums):
  ans = False
  start = 0
  count = 3
  end = len(nums) - 3
  while start <= 5:
    if nums[start:count] == [1, 2, 3]:
      ans = True
      break
    start += 1
    count += 1
  return ans

print array123([1, 1, 2, 3, 1])
print array123([1, 1, 2, 4, 1])
print array123([1, 1, 2, 1, 2, 3])

 # # Note: iterate with length-2, so can use i+1 and i+2 in the loop
 #  for i in range(len(nums)-2):
 #    if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
 #      return True
 #  return False
