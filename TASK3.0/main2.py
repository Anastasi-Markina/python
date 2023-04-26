# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4


def sum(a, b):
    if a == b == 0:
        return 0
    if b == 0:
        return sum(b, a)
    return 1 + sum(a, b-1)


A = int(input())
B = int(input())
print(sum(A, B))
