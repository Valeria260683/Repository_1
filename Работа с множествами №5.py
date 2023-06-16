"""Создать множество set.
Создать неизменяемое множество frozenset.
Выполнить операцию обьединения созданных множеств.
Выполнить операцию пересечения созданных множеств"""
set = {'it', 'is', 'set', 1}
print(set)
frozen_set = frozenset({'it', 'is', 'frozen', 'set', 2})
print(frozen_set)
union = set | frozen_set
print(union)
intersection = set & frozen_set
print(intersection)