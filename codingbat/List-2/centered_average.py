# -*- coding: utf-8 -*-
# Return the "centered" average of an array of ints,
# which we'll say is the mean average of the values,
# except ignoring the largest and smallest values in the array.
# If there are multiple copies of the smallest value,
# ignore just one copy, and likewise for the largest value.
# Use int division to produce the final average.
# You may assume that the array is length 3 or more.
def centered_average(nums):
  nums.sort()
  if len(nums) <= 3:
    return nums[1]
  else:
    del nums[0]
    del nums[len(nums)-1]
    total = 0
    for i in nums:
      total += i
    return total/len(nums)


print centered_average([1, 2, 3, 4, 100]) # 3
print centered_average([1, 1, 5, 5, 10, 8, 7]) # 5
print centered_average([-10, -4, -2, -4, -2, 0]) # -3
print centered_average([1, 2, 100])
