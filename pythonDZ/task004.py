# Требуется определить, можно ли от шоколадки размером n × m долек 
# отломить k долек, если разрешается сделать один разлом по прямой 
# между дольками (то есть разломить шоколадку на два прямоугольника).

m = int(input("Укажите количество долек по вертикали "))
n = int(input("Укажите количество долек по горизонтали "))

k = int(input("Количество долек, которое требуется отломить "))

count = m*n

if k%m == 0 or k%n == 0:
    print("Да, можно отломить")
else:
    print("Нет, нельзя отломить")