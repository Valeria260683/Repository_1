"""Напишите функцию, которая принимает на вход список чисел и возвращает только четные числа из этого списка. """
def list_of_even_numbers(numbers):
    numbers_1 = []
    for number in numbers:
        if number % 2 == 0:
            numbers_1.append(number)
    return numbers_1
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(list_of_even_numbers(numbers))