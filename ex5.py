students_1_sem = [
    {"name": "George", "surname": "Tevzadze", "grades": [5, 5, 5, 4, 5]},
    {"name": "Alice", "surname": "Smith", "grades": [5, 2, 4, 5, 3]},
    {"name": "Bob", "surname": "Stivenson", "grades": [4, 5, 2, 5, 5]},
    {"name": "Aoi", "surname": "Togukawa", "grades": [5, 5, 5, 3, 4, 5, 3]},
    {"name": "Adam", "surname": "Bartelli", "grades": None},
    {"name": "Sylwia", "surname": "Madison", "grades": [3, 5, 4, 3, 3, 5]},
]

students_2_sem = [
    {"name": "George", "surname": "Tevzadze", "grades": [5, 4, 5, 4, 5, 5, 4]},
    {"name": "Alice", "surname": "Smith", "grades": [5, 5, 4, 5, 3, 3, 2, 4]},
    {"name": "Bob", "surname": "Stivenson", "grades": [4, 5, 2, 5, 3]},
    {"name": "Aoi", "surname": "Togukawa", "grades": [5, 5, 5, 5, 4, 5, 3]},
    {"name": "Adam", "surname": "Bartelli", "grades": [3, 3, 5, 4, 3, 5]},
    {"name": "Sylwia", "surname": "Madison", "grades": [5, 5, 4, 3, 4, 5, 3]},
]


def get_best_students(*, students: list[dict]) -> list[dict]:
    best_students = []
    best_average_grade = 0
    for student in students:
        grades = student["grades"]
        if grades is None:
            average_of_grades = 0
        else:
            average_of_grades = sum(grades) / len(grades)

        if average_of_grades > best_average_grade:
            best_average_grade = average_of_grades
            best_students = [student]
        elif best_average_grade == average_of_grades:
            best_students.append(student)

    return best_students


print(get_best_students(students=students_1_sem))
print(get_best_students(students=students_2_sem))
