#Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
#Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
#Пользователь вводит 2 числа.
#n - кол-во элементов первого набора.
#m - кол-во элементов второго набора.
#Значения генерируются случайным образом.

#Input: 11 6
#(значения сгенерированы случайным образом
#2 4 6 8 10 12 10 8 6 4 2
#3 6 9 12 15 18)

#Output: 11 6
#6 12


import random
array1 = int(input('ведите количество элементов первого массива  '))
m = []
for i in range(0,array1):
    random_number = round(random.randint(1,15))
    m.append(random_number)
print(m)

import random
array2 = int(input('ведите количество элементов второго массива  '))
n = []
for i in range(0,array2):
    random_number = round(random.randint(1,15))
    n.append(random_number)
print(n)

res=[]
for i in range(0,array1):
    for j in range(0,array2):
        if m[i]==n[j]:
            res.append(m[i])

#temp = [] 
#for x in res: 
#    if x not in temp: 
#      temp.append(x) 

temp=set(res)
result=list(temp)
result.sort()

print(result)  
   








