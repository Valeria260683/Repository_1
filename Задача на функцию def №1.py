"""Написать функцию date, принимающую 3 аргумента: день, месяц и год. Вернуть True, если такая дата есть
в нашем календаре, False - иначе."""
def date(day, mounth, year):
    if mounth == 2 and day > 28:
       return False
    elif mounth > 0 and mounth < 13 and day > 0 and day < 32 and year > 0:
       return True
    else:
        return False
day = int(input('Ввести день:'))
mounth = int(input('Ввести месяц:'))
year = int(input('Ввести год:'))
print(date(day, mounth, year))