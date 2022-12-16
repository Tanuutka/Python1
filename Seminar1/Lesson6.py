#Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом 
# называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

number_ticket = int(input('Введите номер билета '))
if (abs(number_ticket)< 100000 or abs(number_ticket)> 999999):
    print('Введенное число не шестизначное')
elif (number_ticket < 0):
    print('Номер билета не может быть отрицательным')  
else:
    number_ticket1 = number_ticket//1000
    number_ticket2 = number_ticket%1000
    
sum1=0
sum2=0
while number_ticket1 > 0:
    sum1 += number_ticket1%10
    number_ticket1//=10    
while number_ticket2 > 0:
    sum2 += number_ticket2%10
    number_ticket2//=10        
        
if (sum1==sum2):
    print('Билет счастливый')   
else:
     print('Билет не счастливый')          


   
         