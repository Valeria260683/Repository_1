""" Напишите программу, которая запрашивает у пользователя число n, а затем выводит на экран все числа от n до 1
в обратном порядке."""
n = int(input("Ввести число:"))
for n in range(n, 0, -1):
    print(n)