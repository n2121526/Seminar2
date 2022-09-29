#Задача 3. Реализуйте алгоритм перемешивания списка. Список размерностью 10 задается случайными целыми числами, выводится на экран, затем перемешивается, опять выводится на экран. SHUFFLE нельзя юзать!
import random 
n = 10
sp = []
for i in range(n):
    sp.append(random.randint(1,100))
print(sp)

def mix(sp):
    for i in range(n-1):
        for j in range(n-i-1):
            if sp[j] > sp[j+1]:
                mass = sp[j]
                sp[j] = sp[j+1]
                sp[j+1] = mass
mix(sp)
print(sp)
