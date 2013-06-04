# -*- coding: utf-8 -*-
# Return the number of times that the string "code" appears anywhere
# in the given string,
# except we'll accept any letter for the 'd',
# so "cope" and "cooe" count.
def count_code(str):
  count = 0
  for i in range(0,len(str)-1):
    select = str[i:i+4]
    head = select[0:2]
    tail = select[-1]
    if head == "co" and tail == "e":
      count += 1
  return count

print count_code('aaacodebbb') # 1
print count_code('codexxcode') # 2
print count_code('cozexxcope') # 2
