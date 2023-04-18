# В настольной игре Скрабл (Scrabble) каждая буква имеет 
# определенную ценность. В случае с английским алфавитом очки 
# распределяются так: A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; 
# B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; 
# Q, Z – 10 очков. А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
# Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; 
# Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. Напишите программу, которая вычисляет стоимость 
# введенного пользователем слова. Будем считать, что на вход подается только одно слово, 
# которое содержит либо только английские, либо только русские буквы.


# 1й способ - более лаконичный и приятный
rusLetterPoints = ['АВЕИНОРСТ', 'ДКЛМПУ', 'БГЁЬЯ', 'ЙЫ', 'ЖЗХЦЧ', 'ШЭЮ', 'ФЩЪ']
enLetterPoints = ['AEIOULNSTR', 'DG', 'BCMP', 'FHVWY', 'K', 'JX', 'QZ']
checkPoints = [1, 2, 3, 4, 5, 8, 10]  # список баллов за буквы согласно условию задачи
size = len(checkPoints)

# размеры всех 3х списков равны 7
word = input("Введите слово на русском или английском: ")
count = 0
for i in word.upper():
    for j in range(size):
        if i in rusLetterPoints[j] or i in enLetterPoints[j]:
            count += checkPoints[j]

print(count)

# 2й способ - более развернутый 

# rusLetterOne = 'АВЕИНОРСТ'
# rusLetterTwo = 'ДКЛМПУ'
# rusLetterThree = 'БГЁЬЯ'
# rusLetterFour = 'ЙЫ'
# rusLetterFive = 'ЖЗХЦЧ'
# rusLetterEight = 'ШЭЮ'
# rusLetterTen = 'ФЩЪ'

# enLetterOne = 'AEIOULNSTR'
# enLetterTwo = 'DG'
# enLetterThree = 'BCMP'
# enLetterFour = 'FHVWY'
# enLetterFive = 'K'
# enLetterEight = 'JX'
# enLetterTen = 'QZ'

# word = input("Введите слово на русском или английском: ")
# count = 0
# for i in word.upper():
#     if i in rusLetterOne or i in enLetterOne:
#         count += 1
#     elif i in rusLetterTwo or i in enLetterTwo:
#         count += 2
#     elif i in rusLetterThree or i in enLetterThree:
#         count += 3
#     elif i in rusLetterFour or i in enLetterFour:
#         count += 4
#     elif i in rusLetterFive or i in enLetterFive:
#         count += 5
#     elif i in rusLetterEight or i in enLetterEight:
#         count += 8
#     elif i in rusLetterTen or i in enLetterTen:
#         count += 10
# print(count)

