"""Отсортируйте словарь по значению в порядке возрастания и убывания."""
names = {1: 'Alice', 2: 'John', 4: 'Peter', 3: 'Andrew', 6: 'Ruffalo', 5: 'Chris'}
print(sorted(names.items()))
print(sorted(names.items(), reverse=True))
