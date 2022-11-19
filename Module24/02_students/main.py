class Student:
    def __init__(self, sn, group_number, grade):  # sn-surname & name
        self.sn = sn
        self.group = group_number
        self.grade = grade
        self.average = sum(self.grade)/len(self.grade)

    def print_student(self):
        print('stud name: {}\nStud group: {}\nStud grade: {}'.format(self.sn, self.group, self.grade))

    def average_grade_sort(self):
        return self.average


class StudentsGroup:

    def __init__(self):
        self.student_list = list()
        for number in range(1, 11):
            print()
            self.student_list.append(Student(student_name(number), student_group(), student_grade()))

    def sorted_list(self):
        self.student_list = sorted(self.student_list, key=lambda x: sum(x.grade)/5, reverse=True)
        self.print_student_list()

    def print_student_list(self):
        for stud in self.student_list:
            print()
            stud.print_student()


def student_name(number):
    while True:
        name = input('{})Student\nSurname & name:'.format(number))
        name_list = name.split(' ')
        if len(name_list) == 2 and name_list[0].isalpha() and name_list[1].isalpha():
            return name
        else:
            print('The first and Last name must consist of two WORDS!\nTry again!')


def student_group():
    group_simpl = input('Group number:')
    return group_simpl


def student_grade():
    student_grades_list = list()
    for _ in range(5):
        while True:
            mark = input('Insert grade:')
            if mark.isdigit() and 1 <= int(mark) <= 5:
                student_grades_list.append(int(mark))
                break
            else:
                print('Insert grade from "1" to "5"!')
    return student_grades_list


group_1 = StudentsGroup()
group_1.sorted_list()
