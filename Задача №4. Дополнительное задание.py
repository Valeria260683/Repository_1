"""Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения
(с помощью кортежа): периметр квадрата, площадь квадрата и диагональ квадрата. """
def square(a):
   tuple = (4 * a, a * a, round(2**0.5)*a)
   return tuple
print(square(a = 5))


