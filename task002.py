# В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой 
# грядке, причём кусты высажены только по окружности. Таким образом, у каждого 
# куста есть ровно два соседних. Всего на грядке растёт N кустов. Эти кусты обладают 
# разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод 
# — на i-ом кусте выросло ai ягод. В этом фермерском хозяйстве внедрена система 
# автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких 
# собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед 
# некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать 
# за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном 
# файле грядки.

n = int(input("Укажите количество кустов в грядке: "))
listKust = []

import random
for i in range(n):
    listKust.append(random.randint(1, 10))

print(listKust)

temp = listKust[0]
tempLast = listKust[n-1]
listKust.insert(0, tempLast)
listKust.insert(n+1, temp)

sumThreeNum = 0
for i in range(1, n):
    if listKust[i-1] > sumThreeNum:
        sumThreeNum = listKust[i-1] + listKust[i] + listKust[i+1]
print(temp)
print(tempLast)
print(listKust)
print(f"Максимальный сбор за один заход равен {sumThreeNum}")