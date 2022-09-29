#Задача 1. Напишите программу, которая принимает на вход вещественное или целое число и показывает сумму его цифр. Через строку нельзя решать.

n = str(input('Введите число: '))

def Sum_num(n):
    sp = list(n)
    print(sp)
    for element in sp:   
        if element == ',': 
            sp.remove(',')
    summ = 0
    for element in sp:    
        summ += int(element)
    return summ
    
print(Sum_num(n))