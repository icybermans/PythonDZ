# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, 
# разность и количество элементов нужно ввести с клавиатуры. Формула для получения 
# n-го члена прогрессии: an = a1 + (n-1) * d. Каждое число вводится с новой строки.

a1 = int(input("Укажите первый элемент арифметической прогрессии: "))
d = int(input("Укажите разность арифметической прогрессии: "))
n = int(input("Укажите количество элементов арифметической прогрессии: "))

arif_numbers = []
for i in range(n):
    arif_numbers.append(a1 + d*i)

print(arif_numbers)