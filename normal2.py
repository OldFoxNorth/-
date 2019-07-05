# Задание 1
import math

num = [2, -5, 8, 9, -25, 25, 4]
new_num = []

for el in num:
    if el > 0 and (math.sqrt(el)) % 1 == 0:
        new_num.append(int(math.sqrt(el)))
print(new_num)

# Задание 4
lst = [1, 2, 4, 5, 6, 2, 5, 2]
print(list(set(lst)))

# Задание 3
import random
count = int(input('Введите количество элементов: '))
mylist = []
n = 0
while n < count:
    mylist.append(random.randint(-100, 100))
    n +=1

print(mylist)
