#Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по 
# прямой между дольками (то есть разломить шоколадку на два прямоугольника).

n = int (input('Введите количество долек по горизонтали '))
m = int (input('Введите количество долек по вертикали '))
chokolate = n*m
k = int (input('Введите количество долек которое хотите отломить '))

if n<1 or m<1 or k<1:
    print('Количество долек не может быть меньше или равно 0')
else:
    if (chokolate-k)%n==0 or (chokolate-k)%m==0:
        print('Шоколадку можно разломить по прямой')
    else:  
        print('Шоколадку нельзя разломить по прямой')  
       