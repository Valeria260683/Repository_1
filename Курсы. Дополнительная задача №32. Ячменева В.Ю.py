"""Напишите функцию, которая принимает на вход список строк и возвращает новый список,
содержащий те же строки, но с замененным первым символом на '*'"""
def replacing_character(a):
    new_a = []
    for i in a:
        new_a.append('*' + i[1:])
    return new_a
a = ['apple', 'banana', 'cherry']
print(replacing_character(a))
        