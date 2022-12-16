#Найдите сумму цифр трехзначного числа.
number = int (input('Введите трехзначное число  '))
if (abs(number) < 100 or abs(number) > 999):
    print("Данное число не трехзначное, попробуйте еще раз!")
else:
    print(abs(number)%100//10 + abs(number)%10 + abs(number)//100)
  