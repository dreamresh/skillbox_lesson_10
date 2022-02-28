print('Задача 5. Простые числа')


#Напишите программу,
#которая считает количество простых чисел в заданной последовательности 
#и выводит ответ на экран.

print('Для поиска количества простых чисел в определённом диапазоне необходимо ввести два числа.')
first_number = int(input('Введите первое число диапазона: '))
two_number = int(input('Введите второе чило диапазона: '))

count_prime_number = 0

for number in range(first_number, two_number + 1):
    if (number > 7) and ((number % 2 == 0) or (number % 3 == 0) or (number % 5 == 0) or (number % 7 == 0)):
        continue
    elif (number == 2) or (number == 3):
        count_prime_number += 1
        continue
    else:
        for divisor in range(2, int(number//2)+1):
            if (number % divisor) == 0:
                break
            else:
                count_prime_number += 1
                break

print('Простых чисел в диапазоне с', str(first_number), 'по', str(two_number) + str(':'), str(count_prime_number))
