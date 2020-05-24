import math

def is_primes(num : int) -> bool:
    # ルートを求める計算
    sqrt = math.sqrt(num)
    #is_primeをリストにする
    lists = list(range(2,num+1))
    first = lists[0]
    #先頭がrootの最小まで行う
    if num != 1 and num <= 3:
        return True
    else:
        while lists[0] <= sqrt:
            for num2 in lists:
                if num2 % first == 0 and num2 != first:
                    return False
                else:
                    return True
result = is_primes(4)
print(result)
