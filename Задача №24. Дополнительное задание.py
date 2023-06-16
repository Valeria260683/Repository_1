"""Создать функцию с двумя аргументами, которая вернет массив n-кратных х."""
def count_by(x=2, n=5):
    list = []
    for num in range(1, n+1):
        result = x * num
        list.append(result)
    return(list)
print(count_by(2, 5))
