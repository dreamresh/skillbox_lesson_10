print('Задача 6. Сумма факториалов')

# Напишите программу,
# которая запрашивает у пользователя число N
# и находит сумму факториалов 1! + 2! + 3! +... + N!

number_n = int(input('Введите число: '))


factorial_summ = 0
factorial_count = 0

for x in range(number_n + 1):
    factorial = 1
    for i in range(1, x + 1):
        factorial *= i
        factorial_count = factorial
    print('factorial', x, factorial)
    factorial_summ += factorial_count
print('Сумма факториалов с 1! по', str(number_n) + '!', 'равна', factorial_summ)