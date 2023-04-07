# Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет 
# с номером. Счастливым билетом называют такой билет с шестизначным 
# номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

bilet = int(input("Укажите 6значный номер билета: "))

sum1 = sum2 = 0
k = 0
while bilet > 0:
    if k < 3:
        sum1 += bilet % 10
    else:
        sum2 += bilet % 10
    bilet = bilet//10
    k += 1

if sum1 == sum2:
    print("Билет счастливый")
else:
    print("Билет не счастливый")