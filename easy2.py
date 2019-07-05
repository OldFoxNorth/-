# Задание 1
fruit = ['яблоко', 'банан', 'киви', 'арбуз']
for i, fruits in enumerate(fruit):
    print(i + 1, fruits)
# Вариант 2
fruit1 = 'яблоко'
fruit2 = 'банан'
fruit3 = 'киви'
fruit4 = 'арбуз'
print('{1}: {0}'.format(fruit1, 1))
print('{1}: {0}'.format(fruit2, 2))
print('{1}: {0}'.format(fruit3, 3))
print('{1}: {0}'.format(fruit4, 4))

# Задание 2
list_1 = {1, 3, 5, 3.45, 'ddd'}
list_2 = {8, 9, 0, 3.45, 'ddd'}
list_1 = (list_1 - list_2)
print(list_1)

# Задание 3
lst = [2, 7, 5, 6, 9, 15]
new_lst = [i / 4 if i % 2 == 0 else i * 2 for i in lst]
print(new_lst)