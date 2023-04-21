# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых 
# неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.

# def find_sum_of_two_numbers(a, b):
#     if b == 0:
#         return a
#     return 1 + find_sum_of_two_numbers(a, b - 1)

def find_sum_of_two_numbers(a, b):
    a += 1
    b -= 1
    if b == 0:
        return a
    return find_sum_of_two_numbers(a, b)

a = 13
b = 5
print(find_sum_of_two_numbers(a, b))
