"""Напишите программу на Python для удаления дубликатов из списка."""
original_list = [1, 2, 3, 2, 4, 5, 3]

new_list = list(set(original_list))

print(new_list)