"""Создайте простой калькулятор, который считывает из строки ввода(пример: «1 + 13» три подстроки:
1-ое число, 2-ое число и операцию, после чего применяет операцию к введённым числам, а затем выводит
результат на экран. """
string = input("Enter:")   # "1 + 13"
chars = string.split()     # ['1' '+' '13']
if chars[1] == '+':
    print(int(chars[0]) + int(chars[2]))
elif chars[1] == '-':
    print(int(chars[0]) - int(chars[2]))
elif chars[1] == '*':
    print(int(chars[0]) * int(chars[2]))
elif chars[1] == '/' and chars[2] != '0':
    print(int(chars[0]) / int(chars[2]))
else:
    print("Error")



