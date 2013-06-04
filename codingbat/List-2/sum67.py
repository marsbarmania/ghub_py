# -*- coding: utf-8 -*-
# Return the sum of the numbers in the array,
# except ignore sections of numbers starting
# with a 6 and extending to the next 7
# (every 6 will be followed by at least one 7).
# Return 0 for no numbers.
def sum67(nums):
  if len(nums) == 0: return 0
  count = 0
  if 6 in nums:
    index = 0
    start = False
    while index < len(nums):
      if nums[index] == 6:
        start = True
      # print nums[index]
      if start:
        if nums[index] == 7: start = False
        # print nums[index]
        nums[index] = 0
      index += 1

    for num in nums:
      count += num
  else:
    for num in nums:
      count += num

  return count


print sum67([1, 2, 2]) # 5
print sum67([1, 2, 2, 6, 99, 99, 7]) # 5
print sum67([1, 1, 6, 7, 2]) # 4

# print sum67([1, 6, 2, 2, 7, 1, 6, 99, 99, 7]) # 2
# print sum67([1, 6, 2, 6, 2, 7, 1, 6, 99, 99, 7]) # 2
# print sum67([2, 7, 6, 2, 6, 7, 2, 7]) # 18
# print sum67([2, 7, 6, 2, 6, 2, 7]) # 9

# print sum67([1, 6, 7, 7]) # 8

# print sum67([6, 7, 1, 6, 7, 7]) # 8

# print sum67([6, 8, 1, 6, 7]) # 0
# print sum67([]) # 0
# print sum67([6, 7, 11]) # 11
# print sum67([11, 6, 7, 11]) # 22
# print sum67([2, 2, 6, 7, 7]) # 11
