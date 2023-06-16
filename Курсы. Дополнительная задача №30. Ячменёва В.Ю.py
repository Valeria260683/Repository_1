"""Напишите функцию, которая принимает список строк и возвращает новый список, содержащий
только те строки, которые начинаются с буквы 'а' (большой или малой) """
def my_strings(n):
    new_1 = []
    for i in n:
        if i.startswith('A'):
           new_1.append(i)
        elif i.startswith('a'):
             new_1.append(i)
    return new_1
n = ['Abcn', 'mjhu', 'adsre']
print(my_strings(n))
