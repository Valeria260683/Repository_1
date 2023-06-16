"""Напишите функцию, которая принимает на вход список строк и возвращает список строк,
длина которых больше 5 символов."""
def len_string(string):
    string_1 = []
    for word in string:
        if len(word) > 5:
             string_1.append(word)
    return string_1
string = (["яблоко", "вишня", "клубника", "айва"])
print(len_string(string))
