"""Верните результат умножения если, сумма умножения равна или больше 1000, в противном случае
верните значение суммы двух чисел."""
a = 2000
b = 1000
def product(num1,num2):
    result = num1 * num2
    if result >= 1000:
        print(result)
    else:
        print(num1+num2)

product(a, b)
