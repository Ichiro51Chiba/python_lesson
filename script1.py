import time

t1 = time.time()

def is_prime(num):
    for prime_num in range(2,num):
        if prime_num % 2 == 0:
            pass
        else:      
            prime_num1= print(prime_num)          
is_prime(100)

t2 = time.time()
elapsed_time = t2-t1
print(elapsed_time)
