print('Задача 10. Яма ')


# В одной компьютерной текстовой игре рисуются всяческие элементы ландшафта.
#
# Напишите программу, которая получает на вход число N и выводит на экран числа в виде “ямы”:

# Введите число: 5
#
# 5........5
# 54......45
# 543....345
# 5432..2345
# 5432112345

pit_depth = int(input('Укажите глубину ямы: '))

for row in range(pit_depth):
    count_point = 2 * (pit_depth - row - 1)
    for col_left in range(pit_depth, pit_depth - row - 1, -1):
        print(col_left, end='')
    print(count_point * '.', end='')
    for col_right in range(pit_depth - row, pit_depth + 1):
        print(col_right, end='')
    print()