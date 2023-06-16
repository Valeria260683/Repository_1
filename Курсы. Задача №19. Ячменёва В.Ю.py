"""Написать функцию, принимающую число и возвращающую ближайший к этому числу палиндром."""

def next_palin_drome(n):
    while True:
        n += 1
        if str(n) == str(n)[::-1]:
            return n

n = int(input('Ввести число:'))
print(next_palin_drome(n))









