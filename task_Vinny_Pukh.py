# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке

def is_rytthm_in_poem(glas_stroka = 'аеёиоуыэюя'):
    str_list = input().split()

# 1й способ - через развернутый вложенный цикл, используя метод append()
    # glas_count_array = []
    # for i in str_list:
    #     glas_count = 0
    #     for j in i:
    #         if j in glas_stroka:
    #             glas_count += 1
    #     glas_count_array.append(glas_count)
    # return all(x == glas_count_array[0] for x in glas_count_array)

# 2й способ - через функцию высшего порядка map и lambda (через единый List Comprehension)
    glas_count_stroka = list(map(lambda x: sum(x), [[1 for j in i if j in glas_stroka] for i in str_list]))
    return  all(x == glas_count_stroka[0] for x in glas_count_stroka)

# 3й способ - более развернутая версия 2го способа
    # str_l = [[1 for j in i if j in glas_stroka] for i in str_list]
    # str_res = list(map(lambda x: sum(x), str_l))
    # return str_res

if is_rytthm_in_poem() == True:
    print("Парам пам-пам")
else:
    print("Пам парам")


def is_rytthm_in_poem(str_list):
    str_list = str_list.split()
    glas_stroka = 'аеёиоуыэюя'
    glas_count_stroka = list(map(lambda x: sum(x), [[1 for j in i if j in glas_stroka] for i in str_list]))
    if all(x == glas_count_stroka[0] for x in glas_count_stroka):
        print("Парам пам-пам")
    else:
        print("Пам парам")
