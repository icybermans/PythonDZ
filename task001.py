# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются 
# в обоих наборах. Пользователь вводит 2 числа. n — кол-во элементов первого 
# множества. m — кол-во элементов второго множества. Затем пользователь вводит 
# сами элементы множеств.

n = int(input("Укажите количество элементов в 1м множестве: "))
list_1 = [int(input("Введите число: ")) for i in range(n)]

m = int(input("Укажите количество элементов во 2м множестве: "))
list_2 = [int(input("Введите число: ")) for i in range(m)]

n_mod = set(list_1)
m_mod = set(list_2)

print(list_1)
print(list_2)
mn = n_mod.intersection(m_mod)
mn_list = list(mn)
mn_list.sort()

print(f'Множество ==> {mn}')
print(f'Список ==> {mn_list}')