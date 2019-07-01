# 1
print('Задача 1')
number = int(input('Введите число от 1 до 10: '))
while number <= 0 or number > 10:
    print('неправильно, еще раз')
    number = int(input('Введите число от 1 до 10: '))
print('Верный ввод')
print('Возведение заданного число во вторую степень:', number ** 2)
# 2
print('\nЗадача 2')
number1 = int(input('Введите первое число '))
number2 = int(input('Введите второе число '))
print('Число 1:', number1, '\nЧисло 2:', number2)
# Через сложение и вычитание
number1 = number1 + number2
number2 = number1 - number2
number1 = number1 - number2
print('\nЧисло 1:', number1, '\nЧисло 2:', number2)
# Через умножение и деление (не целочисленное)
number1 = number1 * number2
number2 = number1 / number2
number1 = number1 / number2
print('\nЧисло 1:', int(number1), '\nЧисло 2:', int(number2))
