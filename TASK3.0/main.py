# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8


def rec_degree(a, b):
    if b == 0:
        return 1
    if b > 0:
        return a*rec_degree(a, b-1)
    return rec_degree(a, b+1)/a


A = int(input())
B = int(input())
print(rec_degree(A, B))
