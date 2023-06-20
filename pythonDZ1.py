#Задача 2 Найдите сумму цифр трехзначного числа.
#print("Please input number")
#num = input()
#hundreds = int(num[0])
#dozens = int(num[1])
#units = int(num[2])
#print (hundreds + dozens + units)

#Задача 4 Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, 
#если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
#print ("Please input the sum of cranes")
#s=int(input())
#sergey = s%6
#if (sergey!=0):
#    print("The task conditions are impossible for a given number of cranes")
#else :print (f"Sergey did {s//6} cranes, Petr did {s//6} cranes, Kate did {s*2//3} cranes")

#Задача 6  Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером,
#где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет 
#счастливость билета.
#print ("Please input the ticket number")
#ticket = input()
#a=int(ticket[0])
#b=int(ticket[1])
#c=int(ticket[2])
#d=int(ticket[3])
#e=int(ticket[4])
#f=int(ticket[5])
#if (a+b+c==d+e+f): print("WOW! Ticket - happy")
#else: print ("Sorry - ticket is not happy...")

#Задача 8 Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
#если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
#print("Please input the length of the chocolate bar")
#length=int(input())
#print("Please input the width of the chocolate bar")
#width=int(input())
#print("Please input how many slices do you want to break off")
#slices=int(input())
#if (slices>length*width): print("NO")
#elif(slices<length and slices<width): print("NO")
#elif(slices%length==0 or slices%width==0): print ("YES")






