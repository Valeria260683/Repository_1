"""Передается список, состоящий из строк и букв, нужно вернуть новый список, содержащий только цифры. """
lst = input("Ввести строку:")
num_lst = []
for i in lst:
    if i.isdigit():
        num_lst.append(int(i))
print(num_lst)
