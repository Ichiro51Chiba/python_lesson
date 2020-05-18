# 素数を判定するプログラム

def is_prime(num):
  if num == 1:
    return False

  for prime_num in range(2,num):
    if num % prime_num == 0:
      return False
  return True 

print(is_prime(4))
