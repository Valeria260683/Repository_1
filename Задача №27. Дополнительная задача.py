"""Поменяйте значения а и b местами"""
a = 1000
b = '123'
a, b = b, a
print('"{}"'.format(a))
print(b)