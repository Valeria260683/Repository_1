"""Напишите функцию, которая принимает строку и возвращает список всех уникальных символов в этой строке."""
def get_unique_simbols(string):
    list_of_unique_simbols = []
    for i in string:
        if i not in list_of_unique_simbols:
            list_of_unique_simbols.append(i)
    return list_of_unique_simbols
string = "aaaggghhhtf"
print(get_unique_simbols(string))