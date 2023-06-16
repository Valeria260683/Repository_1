"""Напишите функцию sum_range(start, end), которая суммирует все целые числа от значения «start»
до величины «end» включительно.Если пользователь задаст первое число большее чем второе, просто поменяйте их местами."""
def sum_range(start, end):
    if start < end:
        return sum(range(start, end + 1))
    else:
        return sum(range(end, start + 1))

start = int(input("Введите число:"))
end = int(input("Введите число:"))
print(sum_range(start, end))