"""Напишите программу, которая записывает все содержимое из одного файла в другой,
при этом пропуская строку под номером 5."""
# читаем test.txt
with open("test1.txt", "r") as file:
    # Читаем все строки
    lines = file.readlines()

# Открываем новый файл в режиме записи
with open("new_file.txt", "w") as file:
    count = 0
    for line in lines:
        # Пропускаем 5 линию
        if count == 4:
            count += 1
            continue
        else:
            file.write(line)
        count += 1