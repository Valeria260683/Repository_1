"""Напишите программу, которая запрашивает у пользователя число n, а затем выводит на экран все четные
числа от 2 до n."""
n = int(input("Ввести число:"))
for n in range(2, n):
    if n % 2 == 0:
        print(n)