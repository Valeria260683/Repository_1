"""Написать функцию, которая принимает список целых чисел и проверяет, содержит ли он только простые числа. """
def is_prime(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
        return True


def all_is_prime(array):
    for num in array:
        if is_prime(num) is False:
            return False
    return True


print(all_is_prime([5]))

