class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grades):
        if isinstance(self, Student) and isinstance(lecturer, Lecturer) and \
                course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grades]
            else:
                lecturer.grades[course] = [grades]
        else:
            return 'Ошибка'

    def __str__(self):
        print_student = f'Имя: {self.name}\n' \
                        f'Фамилия: {self.surname}\n' \
                        f'Средняя оценка за домашние задания: {average_rating(self):.2f}\n' \
                        f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
                        f'Завершенные курсы: {", ".join(self.finished_courses)}\n'
        return print_student

    def __lt__(self, other):
        if not isinstance(other, Student):
            return f'Такого студента не существует'
        if average_rating(self) < average_rating(other):
            return f'Средний бал {average_rating(self)} студента {self.surname} меньше среднего бала ' \
                   f'{average_rating(other)} студента {other.surname}'
        else:
            return f'Средний бал {average_rating(self)} студента {self.surname} больше среднего бала ' \
                   f'{average_rating(other)} студента {other.surname}'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor, Student):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        print_lecturer = f'Имя: {self.name}\n' \
                         f'Фамилия: {self.surname}\n' \
                         f'Средняя оценка за лекции: {average_rating(self):.2f}'
        return print_lecturer

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return f'Такого лектора не существует'
        if average_rating(self) < average_rating(other):
            return f'Средний бал {average_rating(self)} лектора {self.surname} меньше среднего бала ' \
                   f'{average_rating(other)} лектора {other.surname}'
        else:
            return f'Средний бал {average_rating(self)} лектора {self.surname} больше среднего бала ' \
                   f'{average_rating(other)} лектора {other.surname}'

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        print_reviewer = f'Имя: {self.name}\n' \
                         f'Фамилия: {self.surname}\n'
        return print_reviewer


# Функцию для подсчета средней оценки вывел отдельно во избежание повтора кода
# Изначально сделал в отдельном классе, оно работало, но ПиЧарму не понравилась такая логистика
def average_rating(human):
    result = 0
    for value in human.grades.values():
        result += sum(value)/len(value)
    return result/len(human.grades.values())

def average_rating_students(students, course):
    count = 0
    average = 0
    for student in students:
        if course in student.courses_in_progress:
            average += sum(student.grades[course])/len(student.grades[course])
            count += 1
    return f'Средний бал студентов по курсу {course}: {average/count:.2f}'

def average_rating_lectors(lecturers, course):
    count = 0
    average = 0
    for lector in lecturers:
        if course in lector.courses_attached:
            average += sum(lector.grades[course])/len(lector.grades[course])
            count += 1
    return f'Средний бал лекторов по курсу {course}: {average/count:.2f}'


first_student = Student('Ruoy', 'Eman', 'm')
first_student.finished_courses += ['Введение в программирование']
first_student.courses_in_progress += ['Python']
first_student.courses_in_progress += ['Git']
second_student = Student('Second', 'Second_Student', 'm')
second_student.finished_courses += ['Введение в программирование']
second_student.courses_in_progress += ['Java']
second_student.courses_in_progress += ['C++']
third_student = Student('Third', 'Third_Student', 'w')
third_student.finished_courses += ['Введение в программирование']
third_student.courses_in_progress += ['Java']
third_student.courses_in_progress += ['Git']

first_reviewer = Reviewer('Some', 'Buddy')
second_reviewer = Reviewer('Second', 'Buddie')
first_reviewer.courses_attached += ['Python']
first_reviewer.courses_attached += ['Java']
second_reviewer.courses_attached += ['Git']
second_reviewer.courses_attached += ['C++']

first_lecturer = Lecturer('First', 'Lecturer_Bud')
second_lecturer = Lecturer('Second', 'Lecturer_Buddie')
first_lecturer.courses_attached += ['Python']
first_lecturer.courses_attached += ['Git']
second_lecturer.courses_attached += ['Java']
second_lecturer.courses_attached += ['C++']
first_student.rate_lecturer(first_lecturer, 'Python', 10)
first_student.rate_lecturer(first_lecturer, 'Git', 10)
second_student.rate_lecturer(second_lecturer, 'Java', 9)
second_student.rate_lecturer(second_lecturer, 'C++', 10)
third_student.rate_lecturer(first_lecturer, 'Git', 9)
third_student.rate_lecturer(second_lecturer, 'Java', 9)

first_reviewer.rate_hw(first_student, 'Python', 8)
first_reviewer.rate_hw(first_student, 'Python', 9)
first_reviewer.rate_hw(first_student, 'Python', 10)
second_reviewer.rate_hw(first_student, 'Git', 9)
second_reviewer.rate_hw(first_student, 'Git', 8)
second_reviewer.rate_hw(first_student, 'Git', 10)
second_reviewer.rate_hw(first_student, 'Git', 9)


first_reviewer.rate_hw(second_student, 'Java', 10)
first_reviewer.rate_hw(second_student, 'Java', 10)
first_reviewer.rate_hw(second_student, 'Java', 10)
second_reviewer.rate_hw(second_student, 'C++', 10)
second_reviewer.rate_hw(second_student, 'C++', 9)
second_reviewer.rate_hw(second_student, 'C++', 10)
second_reviewer.rate_hw(second_student, 'C++', 9)

first_reviewer.rate_hw(third_student, 'Java', 10)
first_reviewer.rate_hw(third_student, 'Java', 9)
first_reviewer.rate_hw(third_student, 'Java', 10)
second_reviewer.rate_hw(third_student, 'Git', 9)
second_reviewer.rate_hw(third_student, 'Git', 9)
second_reviewer.rate_hw(third_student, 'Git', 8)
second_reviewer.rate_hw(third_student, 'Git', 9)

print(first_student)
print(second_student)
print(first_reviewer)
print(second_reviewer)
print(first_lecturer)
print(second_lecturer)
print(third_student)
print(first_student > second_student)
print(first_lecturer < second_lecturer)
print(average_rating_students([first_student, second_student, third_student], 'Python'))
print(average_rating_students([first_student, second_student, third_student], 'Git'))
print(average_rating_lectors([first_lecturer, second_lecturer], 'Java'))
print(average_rating_lectors([first_lecturer, second_lecturer], 'C++'))