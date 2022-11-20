import random


class Parent:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.children = list()

    def add_child(self, child_number):
        for _ in range(child_number):
            child_name = input('Как зовут ребенка?\n')
            while True:
                child_age = int(input('Возраст ребенка?\n'))
                if child_age <= self.age - 16:
                    break
                else:
                    print('Разница в возрасте с родителями должна быть не меньше 16 лет!')
            self.children.append(Children(child_name, child_age))

    def self_info(self):
        print('\nИмя: {}\nВозраст: {}\n'.format(self.name, self.age))
        print('Cписок детей:')
        count = 1
        for kid in self.children:
            print()
            print('{} ребенок:'.format(count))
            kid.info()
            count += 1

    def baby_care(self, index):
        self.children[index].care()

    def baby_food(self, index):
        self.children[index].food()


class Children:

    def __init__(self, name, age):
        self.hungry_meter = ['Голодный', 'Не очень хочет есть', 'Нормально покормлен', 'Объелся']
        self.emotions_meter = ['Плачет', 'Расстроен', 'Спокойный', 'Веселый']
        random_number_1 = random.randint(0, 3)
        random_number_2 = random.randint(0, 3)
        self.child_name = name
        self.child_age = age
        self.hungry_status = self.hungry_meter[random_number_1]
        self.emotion_status = self.emotions_meter[random_number_2]

    def info(self):
        print('Имя:{}.'.format(self.child_name))
        print('Возраст:{}.'.format(self.child_age))
        print('Он {}.'.format(self.hungry_status))
        print('Ребёнок {}!'.format(self.emotion_status))

    def food(self):
        number = self.hungry_meter.index(self.hungry_status)
        if number <= 2:
            self.hungry_status = self.hungry_meter[number+1]
        else:
            print('Все отлично!')

    def care(self):
        number = self.emotions_meter.index(self.emotion_status)
        if number <= 2:
            self.emotion_status = self.emotions_meter[number+1]
        else:
            print('Все отлично!')


def child_check(child_list, condition):
    while True:
        if len(child_list) == 1:
            return 0
        else:
            child_index = int(input('Какого ребенка хотите {}?'.format(condition)))
            index = child_index - 2
            if index <= len(child_list):
                return index+1
            else:
                print('У вас всего {} детей!'.format(len(child_list)))


one = Parent('Ирина', 37)
one.add_child(2)
while True:
    question = int(input('\nЧто вы хотите сделать ? \nЧто бы посмотреть информацияю о себе введите 1.'
                         '\nЧто бы покормить ребенка нажмите 2.\nЧто бы успокоить ребенка нажмите 3.\n'))
    if question == 1:
        one.self_info()
    elif question == 2:
        one.baby_food(child_check(one.children, 'покормить'))
    elif question == 3:
        one.baby_care(child_check(one.children, 'позаботиться'))
    else:
        print('Выберете что то из предложенных вариантов!')


