#Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
#повторениями). Выдать без повторений в порядке возрастания все те числа, которые
#встречаются в обоих наборах.
#Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
#элементов второго множества. Затем пользователь вводит сами элементы множеств
'''
from random import randint
print("spisok 1", list1 := [randint(0,10) for i in range (int(input('please enter size - m: ')))])
print("spisok 2", list2 := [randint(0,10) for i in range (int(input('please enter size - n: ')))])
print("mnojestvo 1", list1 := set(list1))
print("mnojestvo 2", list2 := set(list2))
print ("est' v oboix mnojestvah", list3 := list1.intersection(list1.intersection(list2)))
print ('otsortiruem: ', sorted(list(list3)))
'''

#В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
#круглой грядке, причем кусты высажены только по окружности. Таким образом, у
#каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
#Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
#выросло различное число ягод – на i-ом кусте выросло ai ягод.
#В этом фермерском хозяйстве внедрена система автоматического сбора черники.
#Эта система состоит из управляющего модуля и нескольких собирающих модулей.
#Собирающий модуль за один заход, находясь непосредственно перед некоторым
#кустом, собирает ягоды с этого куста и с двух соседних с ним.
#Напишите программу для нахождения максимального числа ягод, которое может
#собрать за один заход собирающий модуль, находясь перед некоторым кустом
#заданной во входном файле грядки.
'''
from random import randint
print ("плодородность кустов: ", list := [randint(0,10) for i in range (int(input('введите количество кустов на грядке ')))])
print ("sbor yagod", sbor := [list[i-2]+list[i-1]+list[i] for i in range (len(list))])
sbor = sorted(sbor)
print ("maksimal sbor = ", sbor[len(sbor)-1])
'''