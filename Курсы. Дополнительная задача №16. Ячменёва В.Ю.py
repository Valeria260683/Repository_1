""" Написать функцию, которая принимает список строк и сортирует их по возрастанию длины каждой строки."""
def lensort(a):
    return sorted(a, key=len)
print(lensort(["hello","bye","good"]))