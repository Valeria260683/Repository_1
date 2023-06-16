""" Напишите программу которая настроит отображение комментария к отметке 'мне нравится' в условном посте.
Список имен передается в кач-ве аргумента.  """
names = []
if len(names) == 0:
                print("no one likes this")
elif len(names) == 1:
                print(f"{names[0]} likes this")
elif len(names) == 2:
                print(f"{names[0]} and {names[1]} likes this")
elif len(names) == 3:
                print(f"{names[0]}, {names[1]} and {names[2]} likes this")
else:
                print(f"{names[0]}, {names[1]} and {len(names) - 2} other like this")







