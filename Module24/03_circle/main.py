import math


class Circle:
    def __init__(self, horizontal=0, vertical=0, rad=1):
        self.x = horizontal
        self.y = vertical
        self.r = rad

    def square(self, number):
        circle_square = round(math.pi * self.r**2, 2)
        print('\nПлощадь {} окружности равна: {}'.format(number,
                                                         circle_square))

    def perimeter(self, number):
        circle_perimeter = round(2*math.pi*self.r, 2)
        print('\nПериметр {} окружности равна: {}'.format(number,
                                                          circle_perimeter))

    def circle_increase(self, increase_factor, number):
        self.r *= increase_factor
        self.print_parametr(number)

    def print_parametr(self, number):
        print('Координаты центра {} окружности ({}:{}) , радиус:{}'.format(number, self.x, self.y, self.r))


class СoordinateSystem:
    def __init__(self, circle_number):
        self.circle_list = [Circle(coordinate('X'), coordinate('Y'), radius())
                            for _ in range(circle_number)]

    def cirlcle_compariso(self, index):
        circle_number_list = [int(x) for x in range(len(self.circle_list))]
        circle_number_list.remove(index)
        intersection = 0
        for list_index in range(len(circle_number_list)):
            length_line = ((self.circle_list[index].x - self.circle_list[circle_number_list[list_index]].x)**2 +
                           (self.circle_list[index].y -
                            self.circle_list[circle_number_list[list_index]].y)**2)**0.5  #длинна отрезка
                                                                                        # между центрами кругов
            radius_sum = self.circle_list[index].r + self.circle_list[circle_number_list[list_index]].r
            if length_line <= radius_sum:
                print('Окружность {}  пересекается с окружностью {} '.format(index+1, circle_number_list[list_index]+1))
                intersection += 1
        if intersection == 0:
            print('Окружность не пересекается с другими окружностями ')

    def print_circles(self):
        count = 1
        for circle in self.circle_list:
            circle.print_parametr(count)
            count += 1


def coordinate(axis):
    question = input('Хотите задать свои координаты {} ?да/нет'.format(axis)).lower()
    if question == 'да':
        while True:
            coordinate_axis = input('Введите координату {}:'.format(axis))
            if coordinate_axis.isdigit():
                return int(coordinate_axis)
            else:
                print('Необходимо ввести число!')
    else:
        return 0


def radius():
    question = input('Хотите задать свой радиус ?да/нет').lower()
    if question == 'да':
        while True:
            radius_circle = input('Введите радиус круга:')
            if radius_circle.isdigit() and int(radius_circle) > 0:
                return int(radius_circle)
            else:
                print('Необходимо ввести число больше 0 !')
    else:
        return 1


number_of_circle = int(input('Количество кругов которые вы хотите начертить '))
circles = СoordinateSystem(number_of_circle)
circles.print_circles()
while True:
    circle_index = int(input('С какой окружностью из {} будем работать?'.format(number_of_circle)))
    while True:
        first_question = input('\nЕсли хотите найти площадь окружности введите "1".\n'
                               'Если хотите найти периметр окружности введите "2".\n'
                               'Если хотите увеличить радиус окружности введите "3".\n'
                               'Хотите узнать пересекается ли она с другими окружностями?Нажмите "4"')
        if int(first_question) not in [1, 2, 3, 4]:
            print('\nВы ввели неверную команду попробуйте еще раз')
        else:
            if int(first_question) == 1:
                circles.circle_list[circle_index-1].square(circle_index)
            elif int(first_question) == 2:
                circles.circle_list[circle_index - 1].perimeter(circle_index)
            elif int(first_question) == 3:
                ratio = float(input('\nВо сколько раз хотите увеличить радиус окружности?'))
                circles.circle_list[circle_index - 1].circle_increase(ratio, circle_index)
            elif int(first_question) == 4:
                circles.cirlcle_compariso(circle_index-1)
