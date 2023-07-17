#3аполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
#Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
#Каждое число вводится с новой строки.
list =[]
list.insert(0, int(input("please enter the first element ")))
d = int(input("please enter d "))
print (list := [list[0]+(i-1)*d for i in range (1, int(input("please enter the size of progressiv")))])
#Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
'''
from random import randint
print (list := [randint(0,30) for i in range (0,int(input("Please enter the size of massiv  ")))])
min = int(input("Please enter minimum "))
max = int(input("Please enter maximum "))
for i in range (0,len(list)):
    if (list[i] > min):
        if (list[i] < max): 
            print (i)
'''