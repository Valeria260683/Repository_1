""" Создать произвольный словарь -> Добавить новый элемент с ключом типа str и значением типа int
-> Добавить новый элемент с ключом типа кортеж(tuple) и значением типа список(list) -> Получить элемент по ключу
-> Удалить элемент по ключу -> Получить список ключей словаря. """
s = {1: 'Cat', 2: 'Dog', 3: 'Mouse'}
s['str_key'] = 345
print(s)
s[('8', '9', '10')] = ['sunday', 'monday', 33, 44]
print(s)
s.get('str_key')
print(s.get('str_key'))
s.pop('str_key')
print(s)
print(s.keys())