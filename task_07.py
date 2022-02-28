print('Задача 7. Наибольшая сумма цифр')

# Вводится N чисел.
# Среди натуральных чисел, которые были введены,
# найдите наибольшее по сумме цифр. Выведите на экран это число и сумму его цифр.

amount_of_numbers = int(input('Введите количество сравниваемых натуральных чисел: '))
sum_digits_print = 0

for i in range(amount_of_numbers):
    number = int(input('Введите натуральное (целое и положительное) число: '))
    sum_digits = 0
    digits = number
    while digits != 0:
        sum_digits = sum_digits + digits % 10
        digits = digits // 10
    print('Сумма цифр числа', number, 'равна', sum_digits)
    if sum_digits > sum_digits_print:
        number_print, sum_digits_print = number, sum_digits
    elif sum_digits_print == sum_digits:
        print('Сумма цифр чисел', number_print, 'и', number, 'одинаковая')
print('Наибольшим по сумме цифр является число', number_print, 'с суммой цифр равной', sum_digits_print)