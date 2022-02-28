print('Задача 4. Крест')

# Напишите программу,
# которая выводит на экран крест из символов “^”.
#
# (Символы выводятся по диагоналям воображаемого квадрата.)




# ^        ^
#  ^      ^ 
#   ^    ^  
#    ^  ^   
#     ^^    
#     ^^    
#    ^  ^   
#   ^    ^  
#  ^      ^ 
# ^        ^

size_figure = int(input("Укажите размер Х-образного креста: "))


for row in range(size_figure):

    for col in range(size_figure):

        if col == row:
            print("^", end='')
        elif col == (size_figure - row - 1):
            print("^", end='')
        else:
            print(" ", end='')
    print()