# -*- coding: utf-8 -*-

# Given two strings, a and b,
# return the result of putting them together
# in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".

# make_abba('Hi', 'Bye') → 'HiByeByeHi'
# make_abba('Yo', 'Alice') → 'YoAliceAliceYo'
# make_abba('What', 'Up') → 'WhatUpUpWhat'
def make_abba(a, b):
  return a + b*2 + a

print make_abba('Hi', 'Bye')
print make_abba('Yo', 'Alice')
