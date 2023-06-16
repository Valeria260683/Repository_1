"""Написать программу, которая будет конвертировать строку в CamelCase. Например:
"the-stealth-warrior" -> "theStealthWarrior"
"The_Stealth_Warrior" -> "TheStealthWarrior"
"The_Stealth-Warrior" -> "TheStealthWarrior"""
to_delete = "-_"
to_convert = "the-stealth-warrior"
for element in to_convert:
    if element in to_delete:
        to_convert = to_convert.replace(element, "")
        to_convert_lst = to_convert.split()
        print(to_convert_lst)
        result =[to_convert_lst[0]]
        for word in to_convert_lst[1:]:
            result.append(word.capitalize())
            print("".join(result))