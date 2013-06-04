# Given three ints, a b c,
# return True if one of b or c is "close" (differing from a by at most 1),
# while the other is "far", differing
# from both other values by 2 or more.
# Note: abs(num) computes the absolute value of a number.

def close_far(a, b, c):
  # diff1 = abs(a-b)
  # diff2 = abs(a-c)
  # print diff1
  # print diff2
  if abs(a-b)<=1:
    if abs(a-c)>=2<=abs(b-c):
      return True
    else:
      return False
  elif abs(a-c) <=1:
    if abs(a-b)>=2<=abs(b-c):
      return True
    else:
      return False
  else:
    return False




print close_far(1, 2, 10) # True
print close_far(1, 2, 3) # False
print close_far(4, 1, 3) # True
