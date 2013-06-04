# -*- coding: utf-8 -*-

# We want to make a row of bricks that is goal inches long.
# We have a number of small bricks (1 inch each)
# and big bricks (5 inches each).
# Return True if it is possible to make the goal
# by choosing from the given bricks. This is a little harder than it looks
# and can be done without any loops.

def make_bricks(small, big, goal):
  # need_big_blocks = min(B, L div 5) big bricks and (L - 5K) small bricks
  need_big_brick = min(big,goal/5)
  need_small_brick = goal - 5*need_big_brick

  if small >= need_small_brick and big >= need_big_brick:
    return True
  else:
    return False

