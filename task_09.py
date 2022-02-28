print('Задача 9. Пирамидка 2')


# Напишите программу,
# которая получает на вход количество уровней пирамиды и выводит их на экран,

# Пример:
#
#             1
#          3     5
#       7     9     11
#    13    15    17    19
# 21    23    25    27    29

hight = int(input('Укажите высоту пирамиды: '))
print_symbol_count = 1

for i in range(hight):
    string_length = hight - i  # считаем к-во табов слева
    print(string_length * '\t', end='')  # выводим табы слева в строке
    for j in range(i + 1):
        print(print_symbol_count, end='\t\t')
        print_symbol_count += 2
    print()
