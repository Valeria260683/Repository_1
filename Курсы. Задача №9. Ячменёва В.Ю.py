""" "1 2 3 4 5" найдите самое большое и маленькое число в этой строке и верните их кортежем."""
str = input("Ввести строку:")
str_tpl_min = min(map(int, str.split()))
str_tpl_max = max(map(int, str.split()))
str_tpl = str_tpl_min, str_tpl_max
print(str_tpl)





