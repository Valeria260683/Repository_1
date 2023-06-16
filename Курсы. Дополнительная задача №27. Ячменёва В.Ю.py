"""Напишите функцию, которая принимает на вход список строк и возвращает список строк,
которые содержат только цифры."""
def num_list(strings):
    strings_1 = []
    for i in strings:
        for s in i:
         if s.isdigit():
            strings_1.append(int(s))
    return strings_1
strings = ("abc83cde71b24","56687dfgkl8976")
print(num_list(strings))

"""Напишите функцию, которая принимает на вход список строк и возвращает список строк,
которые содержат только цифры."""
def num_list(strings):
    strings_1 = []
    for i in strings:
        if i.isdigit():
            strings_1.append(i)
    return strings_1
strings = ("574","566", "ghgjh", "gjgh")
print(num_list(strings))


