def read_subjects() -> list:
    """Считывает список предметов."""
    subjects = []
    while True:
        subject = input("Введите предмет: ")
        if subject.lower() == "стоп":
            break
        subjects.append(subject)
    return subjects


def read_students() -> list:
    """Считывает список студентов (фамилия, имя)."""
    students = []
    while True:
        name = input("Введите фамилию и имя студента (через пробел): ")
        if name.lower() == "стоп":
            break
        try:
            surname, name = name.split()
            students.append((surname, name))
        except ValueError:
            print("Ошибка: Введите фамилию и имя через пробел.")
    return students


def read_scores(students, subjects) -> list:
    """
    Считывает оценки студентов по предметам.
    Возвращает список словарей, где каждый словарь представляет оценки одного студента.
    """
    scores = []
    for student in students:
        student_scores = {}
        print(f"Оценки для студента {student[0]} {student[1]}:")
        for subject in subjects:
            while True:
                try:
                    score = int(input(f"Введите оценку по предмету {subject} для студента {student[0]} {student[1]}: "))
                    if 1 <= score <= 10:
                        student_scores[subject] = score
                        break
                    else:
                        print("Оценка должна быть в диапазоне от 1 до 10.")
                except ValueError:
                    print("Ошибка: Введите целое число.")
        scores.append(student_scores)
    return scores


def statistics(students: list, scores: list, subjects: list):
    """Вычисляет статистику успеваемости."""

    # Вычисление средней успеваемости каждого студента
    student_averages = {}
    for i, student in enumerate(students):
        total_score = sum(scores[i].values())
        average_score = total_score / len(scores[i])
        student_averages[student] = average_score

    # Определение студента с лучшей успеваемостью
    best_student = max(student_averages, key=student_averages.get)
    best_average = student_averages[best_student]

    # Вычисление среднего балла по каждому предмету
    subject_averages = {}
    for subject in subjects:
        total_score = 0
        count = 0
        for student_scores in scores:
            if subject in student_scores:
                total_score += student_scores[subject]
                count += 1
        if count > 0:
            subject_averages[subject] = total_score / count
        else:
            subject_averages[subject] = 0  # Если никто не сдавал предмет

    return best_student, best_average, subject_averages


# Основная часть программы
subjects = read_subjects()
students = read_students()
scores = read_scores(students, subjects)

if students and subjects and scores:  # проверяем что есть данные, иначе может вылететь ошибка
    best_student, best_average, subject_averages = statistics(students, scores, subjects)

    print("\nРезультаты:")
    print(
        f"Студент с лучшей средней успеваемостью: {best_student[0]} {best_student[1]} (средний балл: {best_average:.2f})")

    print("\nСредний балл по предметам:")
    for subject, average in subject_averages.items():
        print(f"{subject}: {average:.2f}")
else:
    print("Не введены данные о предметах, студентах или оценках.")
