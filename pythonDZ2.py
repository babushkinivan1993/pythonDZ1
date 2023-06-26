#Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, 
#чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
#from random import randint
#print ("How many coins are on the table")
#coins = int(input())
#eagle, tails = 0,0
#for side in range(coins):
#    side = randint(0,1)
#    print (side, end=" ")
#    if (side==0): eagle += 1
#    else: tails += 1
#if (eagle < tails): print (f"\nThe minimum required number of coups {eagle}")
#else: print (f"\nThe minimum required number of coups - {tails}")

#Задача 12 Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
#Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
#Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
#print ("Please enter summ of the numbers")
#summa = int(input())
#print ("Please enter composition of the numbers")
#composition = int(input())
#b=summa*-1
#d=summa*summa - 4*composition
#if (d<0): print ("Problem has no solution")
#else: print (f"Numbers are {(d**0.5-b)/2} and {composition/((d**0.5-b)/2)}")

#Задача 14 Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
#print ("Please enter number N")
#n=int(input())
#k=0
#while (2**k<n): 
#    print (2**k, end=" ")
#    k +=1
