"""С клавиатуры вводится натуральное число. Найти его наибольшую цифру. Например, введено число 764580.
Наибольшая цифра в нем 8."""
num = input('Введите число:')
str_num = str(num)
lst_num = list(num)
print(int(max(lst_num)))
