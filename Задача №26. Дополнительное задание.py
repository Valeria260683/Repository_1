"""Посчитать сумму чисел от 0 до number"""
number = int(input('Ввести число:'))
summa = 0
for i in range(number + 1):
    summa += i
print(summa)