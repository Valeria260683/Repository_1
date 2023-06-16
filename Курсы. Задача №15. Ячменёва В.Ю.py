""" Дан список чисел. Реализуйте "bubble sort" для этого списка и верните, получившееся значение."""
lst = [20, 17, 14, 15, 16, 11, 9, 10, 5, 7, 4, 3, 8, 2]
n = 14
count = 0
for run in range(n-1):
    for i in range(n-1):
        if lst[i] >= lst[i+1]:
            count += 1
            lst[i], lst[i+1] = lst[i+1], lst[i]
            print(lst)
            print(count)
