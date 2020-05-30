# フィボナッチ数列をやってみる

def fib_num(num):

    if num == 1:
        return 0
    if num == 2:
        return 1
    if num <= 2:
        return num

    return fib_num(num - 2) + fib_num(num - 1)

result = fib_num(10)
print(result)


