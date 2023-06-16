"""Отсортируйте словарь по значению в порядке возрастания и убывания."""

dict = {'a': '100', 'b': 120, 'c': 130, 'd': 140}
print(sorted(dict.items()))
print(sorted(dict.items(), reverse= True))


