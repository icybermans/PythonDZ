# Требуется найти в массиве A[1..N] самый близкий по величине элемент 
# к заданному числу X. Пользователь в первой строке вводит натуральное 
# число N – количество элементов в массиве. В последующих  строках записаны 
# N целых чисел Ai. Последняя строка содержит число X

size = int(input("Укажите размер массива: "))
listHome = [int(input("Введите число: ")) for i in range(size)]

k = int(input("Укажите пороговое значение: "))

minDiff = abs(k - listHome[0])
num = listHome[0]
num2 = listHome[0]

for i in range(1, size):
    if abs(k - listHome[i]) < minDiff:
        minDiff = abs(k - listHome[i])
        num = listHome[i]
    if minDiff == abs(k - listHome[i]) and listHome[i] != num:
        num2 = listHome[i]
        

if num2 == num:
    print(f"Самое близкое по величине значение к числу {k} - {num}")
else:
    print(f"Введение значение {k} находится между {num} и {num2}")
