#Напишите программу, которая на вход принимает два числа A и B,
#и возводит число А в целую степень B с помощью рекурсии.

def Degree(x,y):
    if y>0:
        return x*Degree(x,y-1)
    else: return 1    

x=int(input())
y=int(input())
res=Degree(x,y)

print(res)