def is_prime(x):
  # 2は素数
  if x == 2:
    return True
  # 2以下または偶数は素数ではない
  if x < 2 or x % 2 == 0:
    return False

  for i in range(2,x-1,1):
    if x % i == 0:
      return False
  return True

def primenumber_count(num):
  count = 0
  for i in range(num):
    if is_prime(i):
      count += 1
  return count

print(primenumber_count(2))
