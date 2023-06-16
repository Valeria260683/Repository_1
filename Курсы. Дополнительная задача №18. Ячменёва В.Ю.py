"""Написать функцию, которая принимает список словарей, где каждый словарь представляет собой
запись об ученике (с ключами 'имя', 'возраст', 'оценки'), и возвращает список словарей,
отсортированный по возрасту учеников в порядке убывания средней оценки каждого ученика."""
students = [{"name": "John", "age": 24, "marks": [3, 5, 4, 2]},
{"name": "Kelly", "age": 20, "marks": [2, 5, 4, 3]},
{"name": "Maks", "age": 22, "marks": [2, 3, 4, 5]},
{"name": "Alice", "age": 21, "marks": [4, 4, 4, 5]}]
def students_dict(students):
    def average_marks(student):
        marks = student['marks']
        return sum(marks) / len(marks)

    sorted_students = sorted(students, key=lambda x: (x['age'], -average_marks(x)), reverse=True)
    return sorted_students
print(students_dict(students))