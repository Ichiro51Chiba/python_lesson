# 素数を判定するプログラム

# def is_prime(num):
#   if num == 1:
#     return False

#   for prime_num in range(2,num):
#     if num % prime_num == 0:
#       return False
#   return True 

# print(is_prime(4))

# def is_prime(num):
#     for prime_num in range(2,num):
#         if prime_num % 2 == 0:
#             pass
#         else:      
#             prime_num1= print(prime_num)
            
# is_prime(31)


#################################################
# エラトステネスのふるい
import time

t1 = time.time()

def is_primes(num):
    for is_prime in range(1,num):
        if is_prime == 1:
            continue
        if is_prime != 2 and is_prime % 2 == 0:
            continue
        if is_prime != 3 and is_prime % 3 == 0:
            continue
        if is_prime != 5 and is_prime % 5 == 0:
            continue
        if is_prime != 7 and is_prime % 7 == 0:
            continue
        if is_prime !=11 and is_prime % 11 == 0:
            continue
        print(is_prime)

is_primes(100)

t2 = time.time()
elapsed_time = t2-t1
print(elapsed_time)

##################################################