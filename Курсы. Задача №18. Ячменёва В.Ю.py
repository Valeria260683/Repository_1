"""Написать функцию, которая принимает список и считает кол-во одинаковых элементов в нем."""
def get_many_numbers(numbers):
    x = {i for i in numbers if numbers.count(i) > 1}
    return len(x)
sequence = input('Input: ').split(',')
print(get_many_numbers(sequence))