#На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
#Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
#Выведите минимальное количество монет, которые нужно перевернуть.
import random
n = int(input('ведите число  '))
m = []
count1=0
count2=0 
for i in range(0,n):
    random_number = round(random.randint(0,1))
    m.append(random_number)
    if m[i]==0: count1+=1
    if m[i]==1: count2+=1 
if count1>count2: turn_iver_num = count2
else: turn_iver_num = count1

print(m)
print("Минимальное количество монет, которое нуно перевернуть равно ", turn_iver_num)