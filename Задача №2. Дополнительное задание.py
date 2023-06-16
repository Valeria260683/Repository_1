"""Напишите программу для слияния нескольких словарей в один."""
dictA = {'alice': 12, 'emma': 16, 'eric': 19}
dictB = {'jack': 18, 'kevin': 15, 'teona': 14}
dictA.update(dictB)
print('Updated dictionary A :')
print(dictA)