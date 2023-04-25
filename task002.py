# Задача 32: Определить индексы элементов массива (списка), значения которых 
# принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше 
# заданного максимума)

min_value = int(input("Укажите нижнюю границу интервала: "))
max_value = int(input("Укажите верхнюю границу интервала: "))

n = int(input("Укажите количество элементов в генерируемом списке: "))

import random

def generate_random_array(n):
    list_random_numbers = []
    for i in range(n):
        list_random_numbers.append(random.randint(1, 100))
    return list_random_numbers

def find_list_indeces(mx, mn, current_list):
    list_indeces = []
    for i in range(len(current_list)):
        if current_list[i] >= mn and current_list[i] <= mx:
            list_indeces.append(i)
    return list_indeces

generate_list = generate_random_array(n)
result = find_list_indeces(max_value, min_value, generate_list)

print(generate_list)
print(result)