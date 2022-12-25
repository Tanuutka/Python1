#Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
#Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
#Заполните массив случайными натуральными числами от 1 до N.
#Выведите, ближайший к X элемент. Если есть несколько элементов, которые равноудалены от X, выведите наименьший по величине.

import random
n = int(input('ведите количество элементов массива  '))
m = []
for i in range(0,n):
    random_number = round(random.randint(1,n))
    m.append(random_number)
print(m)
import math
x= int(input('введите число '))
min=abs(x-m[0])
min_index=0
for i in range(0,n-1):
    if abs(x-m[i]) < min:
        min=abs(x-m[i])
        min_index=i
        if min == abs(x-m[i]):
            if m[min_index]<=m[i]:
                min_index=min_index
            else: min_index =i
print(m[min_index])