print('Медицинская анкета')
name = input('Введите имя: ')
family = input('Введите Фамилию: ')
age = int(input('Введите возраст: '))
weight = int(input('Введите вес '))
if age < 30 and 120 >= weight >= 50:
    print('\nПациент:', name, family, '\nВ хорошем состоянии', '\nвозраст:', age, '\nвес:', weight)
elif 39 >= age >= 31 and (weight < 50 or weight > 120):
    print('\nПациент:', name, family, '\nТребуется начать вести правильный образ жизни', '\nвозраст:', age, '\nвес:', weight)
elif age >= 40 and (weight < 50 or weight > 120):
    print('\nПациент:', name, family, '\nТребуется врачебный осмотр', '\nвозраст:', age, '\nвес:', weight)