# -*- coding: utf-8 -*-
import math

num = 9





def master():
    print("master")
    
def master1():
    print("master1")


def sieve_of_eratosthenes(target):
    dest = int(math.sqrt(target))
    lists = list(range(2, target + 1))
    prime_list = []

    while True:
        num_min = min(lists)
        if num_min > dest:
            prime_list.extend(lists)
            break
        prime_list.append(num_min)

        i = 0

        while True:
            if i >= len(lists):
                break
            elif lists[i] % num_min == 0:
                lists.pop(i)
            i += 1

    print(num in prime_list)

sieve_of_eratosthenes(num)
