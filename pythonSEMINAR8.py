def print_menu() :
    print("1. Открыть файл")
    print("2. Сохранить файл")
    print("3. Показать контакты")
    print("4. Добавить контакты")
    print("5. Найти контакт")
    print("6. Изменить контакт")
    print("7. Удалить контакт")
    print("8. Выход")
    print("Выберите необходимый функционал ")
def print_the_book (list):
    maxlen = 0
    for i in list:
        if (len(i[0])>maxlen): maxlen = len(i[0])+4
    for i in list:
        print (i[0] + (maxlen-len(i[0]))*" " + i[1] + "   " + i[2] + "\n")
def next ():
    print(("Если хотите продолжить работу напишите Y"))
    print(("Если хотите завершить работу напишите N"))
    if (input() == "Y"):return 1
    return 8
print_menu()
press = int(input())
while (press >0 and press<8 ):
    data = open('telephonebook.txt', 'r')
    list = [line.split(";") for line in data]
    if (press == 1):
        print ("                    СИСТЕМНОЕ СООБЩЕНИЕ: Файл уже открыт")
        print_menu()
        press = int(input())
    if (press == 3): 
        print_the_book(list)
        press = next()
    if (press == 4):
        data.close
        data = open('telephonebook.txt', 'a')
        data.write("\n")
        data.write(input("Добавьте новый контакт в формате: Фамилия(на латинице);номер телефона;должность\n"))
        print("Контакт добавлен")
        press = next()   
    if (press == 5):
        information = input("Введите фамилию(на латинице)\n")
        for i in list: 
            if (information == i[0]): 
                print (*i)
            #print (i[2])
            #print (information)
        press=next()
    if (press == 6):
        print_the_book(list)
        contact = input("Чей контакт вы хотите изменить?\n")
        change = input ("Что необходимо поменять? surname / telephone / profession?\n")
        for i in list:
            if (contact == i[0]):
                if(change=="surname"):i[0]=input("Введите новую фамилию\n")
                if(change=="telephone"):i[1]=input("Введите новый телефон\n")
                if(change=="profession"):i[2]=input("Введите новую профессию\n")
        data.close
        data = open('telephonebook.txt', 'w')
        for i in list:
            data.writelines(i[0])
            data.writelines(";")
            data.writelines(i[1])
            data.writelines(";")
            data.writelines(i[2])
        press = next()
    if (press ==7):
        print_the_book(list)
        contact = input("Чей контакт вы хотите удалить?\n")
        flag=True
        i=0
        while(i<len(list) and flag==True):
            for j in list[i]:
                if (contact == j):
                    list.pop(i)
                    flag=False
            i+=1        
        data.close
        data = open('telephonebook.txt', 'w')
        for i in list:
            data.writelines(i[0])
            data.writelines(";")
            data.writelines(i[1])
            data.writelines(";")
            data.writelines(i[2])
        press = next()
    data.close
