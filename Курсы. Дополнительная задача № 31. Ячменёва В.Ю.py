"""Напишите функцию, которая принимает на вход список чисел, и возвращает новый список,
содержащий только те числа, которые больше среднего значения всех чисел в списке."""
def filter_above_average(numbers):
    average = sum(numbers) / len(numbers)
    result = []
    for num in numbers:
        if num > average:
            result.append(num)
    return result
numbers = [1, 2, 3, 4, 5]
print(filter_above_average(numbers))