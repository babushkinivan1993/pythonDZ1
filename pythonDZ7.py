#Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
#Вам стоит написать программу. Винни-Пух считает, что 
#ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
#Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. 
#Фразы отделяются друг от друга пробелами. 
#Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
def count_glasn (string):
    count = 0
    for i in string:
        if (i=="а" or i=="е" or i=="ё" or i=="и" or i=="о" or i=="у" or i=="э" or i=="ю" or i=="я"): count += 1
    return count
def bit (string):
    listok = stih.split(" ")
    for i in range (1, len(listok)):
        if (count_glasn(listok[i]) != count_glasn(listok[i-1])): return "Пам парам"
    return "Парам пам-пам"
stih = input("Винни, вводи свой стих ")
print (bit(stih))

#Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента функцию, вычисляющую элемент 
#по номеру строки и столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы 
#(подумайте, почему не с нуля). 
#Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.
'''
def print_opearation_table (operation, num_rows, num_columns):
    for i in range(1,num_rows+1):
        print("\n")
        for j in range (1,num_columns+1):
            print(operation(i,j), end =" ")
print_opearation_table(lambda x,y: x*y,6,6)

# не смог причесать, чтобы смотрелось красиво. Подскажите пожалуйста
'''