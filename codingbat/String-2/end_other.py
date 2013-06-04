# -*- coding: utf-8 -*-
# Given two strings,
# return True if either of the strings appears at the very end of the other string,
# ignoring upper/lower case differences
# (in other words, the computation should not be "case sensitive").
# Note: s.lower() returns the lowercase version of a string.

def end_other(a, b):
  a = a.lower()
  b = b.lower()
  if a in b:
    return True if a[-len(a)::]==b[-len(a)::] else False
  elif b in a:
    return True if b[-len(b)::]==a[-len(b)::] else False
  else:
    return False

# Solution:

# def end_other(a, b):
#   a = a.lower()
#   b = b.lower()
#   return (b.endswith(a) or a.endswith(b))

# print "===== should be True ====="
print end_other('Hiabc', 'abc') # True
print end_other('AbC', 'HiaBc') # True
print end_other('abc', 'abXabc') # True
print end_other('Hiabc', 'bc') # True
print end_other('abc', 'abc') # True
print end_other('xyz', '12xyz') # True
print end_other('Z', '12xz') # True
print end_other('12', '12') # True
print end_other('ab', '12ab') # True

print "===== should be False ====="
print end_other('Hiabc', 'abcd') # False
print end_other('Hiabcx', 'bc') # False
print end_other('yz', '12xz') # False
print end_other('abcXYZ', 'abcDEF') # False
print end_other('ab', 'ab12') # False
