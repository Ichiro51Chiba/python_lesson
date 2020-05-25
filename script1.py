import math

def is_primes(num : int) -> bool:
    # ルートを求める計算
    sqrt = math.sqrt(num)
    #is_primeをリストにする
    lists = list(range(2,num+1))
    new_lists = [2]
    #先頭がrootの最小まで行う
    if num != 1 and num <= 3:
        return True
    else:
        while lists[0] <= sqrt:
            for num2 in new_lists:
                if num2 % lists[0] == 0 and num2 != lists[0]:
                    return False
                else:
                    new_lists.append(lists[0])
                    del lists[0]
result = is_primes(5)
print(result)
