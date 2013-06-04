# -*- coding: utf-8 -*-
# Return True
# if the given string contains an appearance of "xyz"
# where the xyz is not directly preceeded by a period (.).
# So "xxyz" counts but "x.xyz" does not.
def xyz_there(str):
  if "xyz" in str:
    # 連続する場合
    if str[str.index('xyz')-1]=='.':
      str = str.replace('.xyz','')
      return True if 'xyz' in str else False
    else:
      return True
  else:
    return False

print xyz_there('abcxyz') # True
print xyz_there('abc.xyz') # False
print xyz_there('xyz.abc') # True

print xyz_there('abc.xyzxyz') # True

