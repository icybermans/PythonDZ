# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.

def print_operation_table(operation, num_rows=6, num_columns=6):

# ----------- 1й способ ----------
    # for i in range(1, num_rows + 1):
    #     for j in range(1, num_columns + 1):
    #         print(f'%3d' %(operation(i, j)), end = ' ')
    #     print()

# ---------- 2й способ - сырой-----------
    # print([[operation(i, j) for i in range(1, num_rows + 1)] 
    #                             for j in range(1, num_columns + 1)])

# ---------- 2.1й способ ----------
    # for i in [[operation(i, j) for i in range(1, num_rows + 1)] for j in range(1, num_columns + 1)]: 
    #     for j in i:
    #         print(f'%3d' %(j), end = ' ')
    #     print()

# ---------- 3й способ -----------
    return list(map(lambda x: print(f'{x}'),[[operation(i, j) for i in range(1, num_rows + 1)] for j in range(1, num_columns + 1)]))
print_operation_table(lambda x, y: x * y)



