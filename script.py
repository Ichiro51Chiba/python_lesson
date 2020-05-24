# # # 素数を判定するプログラム

# # def is_prime(num):
# #   if num == 1:
# #     return False
# #   for prime_num in range(2,num):
# #     if num % prime_num == 0:
# #       return False
# #   return True 

# # # print(is_prime(4))

# # # def is_prime(num):
# # #     for prime_num in range(2,num):
# # #         if prime_num % 2 == 0:
# # #             pass
# # #         else:      
# # #             prime_num1= print(prime_num)
            
# # # is_prime(31)


# # #################################################
# # # エラトステネスのふるい
# # # import time
# # # # t1 = time.time()

# # # def is_primes(num:int) -> int:
# # #   if num == 1:
# # #     return False

# # #   for is_prime in range(2,num):
# # #     if is_prime != 2 and is_prime % 2 == 0:
# # #         return False
# # #     if is_prime != 3 and is_prime % 3 == 0:
# # #         return False
# # #     if is_prime != 5 and is_prime % 5 == 0:
# # #         return False
# # #     if is_prime != 7 and is_prime % 7 == 0:
# # #         return False
# # #     if is_prime !=11 and is_prime % 11 == 0:
# # #         return False

# # # print(is_primes(1))

# # # t2 = time.time()
# # # elapsed_time = t2-t1
# # # print(elapsed_time)

# # ##################################################

# import math

# def is_primes(num : int) -> bool:
#     # ルートを求める計算
#     sqrt = math.floor(math.sqrt(num))
#     #is_primeをリストにする
#     lists = list(range(2,num+1))
#     first = lists[0]
#     #先頭がrootの最小まで行う
#     # while lists[0] <= sqrt:
#     lists = [num2/first for num2 in lists]
#     return lists
# result = is_primes(4)
# print(result)

