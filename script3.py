from script import is_prime
from typing import Callable
import time

def count_time(func,*args,**kwargs):
  t1 = time.time()
  result = func(*args,**kwargs)
  t2 = time.time()
  elapsed_time = t2-t1
  print(elapsed_time)
  return result

result = count_time(is_prime,485532119)
print("result:",result)

# 関数のラップ処理

