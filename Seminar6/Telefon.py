#Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер 
# телефона - данные, которые должны находиться в файле.
#Программа должна выводить данные
#Программа должна сохранять данные в текстовом файле
#Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
#Использование функций. Ваша программа не должна быть линейной

fileName = 'tel.txt'


def writeFile(file_name):
    r=input("Введите имя для добавления: ")
    with open(file_name, 'a', encoding='UTF-8') as data:
        data.writelines(r + '\n')
    print('Абонент успешно добавлен')

def readFile(file_name):
    result = []
    with open(file_name, 'a', encoding='UTF-8') as data:
        for line in data:
            result.append(line.split())
    return result



def readFile2(file_name):
    result = []
    with open(file_name, 'r', encoding='UTF-8') as data:
        for line in data:
            result.append(line.split())
    return result

def findUsers(userList):
    name = input("Введите имя для поиска: ")

    for user in userList:
        if user[1]== name or user[0] == name or user[2]  == name:
            print(user[3])
      
def findTelefone(telefonList):
    name = input("Введите телефон для поиска: ")

    for user in telefonList:
        if user[-1]== name:
            print(user)

def replacementTelefone(telefonReplacement):
    name = input("Введите имя абонента, номер которого нужно изменить: ")
    replacement=input("Введите новый номер: ")
    for user in telefonReplacement:
        if user[0]== name or user[1]== name or user[2]== name:
           
            for i in user:
            
                with open(fileName, 'r', encoding='UTF-8') as data:
                   old_data = data.read()

            new_data = old_data.replace(user[-1], replacement)

            with open (fileName, 'w', encoding='UTF-8') as f:
                 f.write(new_data)
    print('Номер абонента изменен')

def delete(delete_user):
    import csv
    name = input("Введите фамилию абонента, номер которого нужно удалить: ")
    for user in delete_user:
        if user[0]== name:
            deleie_name = delete_user.remove(user)
            break
    with open(fileName, 'w',newline='', encoding='UTF-8') as csv_file:
        writer = csv.writer(csv_file, delimiter=' ',quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        for row in delete_user:
            writer.writerow(row)



while True:
    print("1. Вывести на экран список всех абонентов")
    print("2. Добавить абонента")
    print("3. Найти номер по имени абонента")
    print("4. Найти абонента по номеру телефона")
    print("5. Изменить номер абонента")
    print("6. Удалить номер абонента")
    print("0. Выйти из меню")
    n = input("Выберите пункт: ")
    
    if n == "1":
        print(readFile2(fileName))
    elif n == "2":
        print(readFile2(fileName))
        writeFile(fileName)
    elif n == "3":
        print(readFile2(fileName))
        findUsers(readFile2(fileName))
    elif n == "4":
        print(readFile2(fileName))
        findTelefone(readFile2(fileName))
    elif n == "5":
        print(readFile2(fileName))
        replacementTelefone(readFile2(fileName))  
    elif n == "6":
        print(readFile2(fileName))
        delete(readFile2(fileName))
    elif n == "0":
        break
    else:
        print("Вы ввели не правильное значение")

#writeFile(fileName)
#print(readFile2(fileName))
#print(type(readFile(fileName)))
#findUsers(readFile2(fileName))
#findTelefone(readFile2(fileName))
#replacementTelefone(readFile2(fileName))
#print(readFile2(fileName))
#delete(readFile2(fileName))

