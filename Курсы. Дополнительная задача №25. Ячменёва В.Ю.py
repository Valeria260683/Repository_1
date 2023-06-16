"""Напишите функцию, которая принимает на вход список строк и возвращает список строк,
которые содержат букву "e"."""
def list_of_string(string):
    string_1 = []
    for element in string:
        if "е" in element:
            string_1.append(element)
    return string_1
string = (["белый", "небо", "поле", "река", "осадок", "дождь", "зима"])
print(list_of_string(string))