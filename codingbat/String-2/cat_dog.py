# -*- coding: utf-8 -*-
# Return True
# if the string "cat" and "dog" appear the same number of times
# in the given string.

def cat_dog(str):
  cat = 0
  dog = 0
  for i in range(len(str)-1):
    current = str[i:i+3]
    if current == 'cat':
      cat +=1
    elif current == 'dog':
      dog += 1
  if cat == dog:
    return True
  else:
    return False

# print cat_dog('catdog') # True
# print cat_dog('catcat') # False
# print cat_dog('1cat1cadodog') # True
print cat_dog('ca') # True
print cat_dog('c') # True
print cat_dog('') # True
