"""Напишите программу на Python, чтобы получить список, отсортированный в порядке возрастания
по последнему элементу в каждом кортеже из заданного списка непустых кортежей."""
list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
def last(n):
    return n[-1]

def sort_list_last(tuples):
        return sorted(tuples, key=last)

print(sort_list_last(lst))