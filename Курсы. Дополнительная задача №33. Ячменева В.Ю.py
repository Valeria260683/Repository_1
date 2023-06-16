"""Напишите функцию, которая принимает на вход список списков чисел и возвращает
новый список, содержащий те же числа, увеличенный на 1"""
def increase_lists(numbers):
    result = []
    for num in numbers:
        new_numbers = []
        for i in num:
            new_numbers.append(i + 1)
        result.append(new_numbers)
    return result
numbers = ([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(increase_lists(numbers))