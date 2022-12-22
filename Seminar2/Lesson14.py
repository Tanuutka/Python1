#Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
n = int(input('ведите число N '))
i=0
digree=0
while digree < n-2**(i-1):
    digree = 2**i
    print (digree)
    i+=1
    

