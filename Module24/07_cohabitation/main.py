import random


class Human:
    def __init__(self, name):
        self.name = name
        self.satiety = 50

    def play(self):
        self.satiety -= 2
        print('{} сел поиграть'.format(self.name))

    def work(self, room):
        print('{}  пошел на работу.'.format(self.name))
        room.vault += 10
        self.satiety -= 3

    def eating(self, room):
        self.satiety += 3
        room.fridge -= 4
        print('{} сел покушать'.format(self.name))

    def shoping(self, room):
        print('{}  пошел в магазин.'.format(self.name))
        room.vault -= 5
        room.fridge += 5

    def death_check(self):
        if self.satiety <= 0:
            return True

    def status(self):
        print('{} :\n Сытость:{}'.format(self.name, self.satiety))


class Home:
    def __init__(self):
        self.fridge = 50
        self.vault = 0
        self.room_mates = list()

    def add_room_mate(self):
        roomates_number = int(input('Сколько человек будет жить в квартире ? '))
        for number in range(roomates_number):
            roommate_name = input('Введите имя {} соседа:'.format(number+1))
            self.room_mates.append(Human(roommate_name))

    def home_status(self):
        print('В холодильнике:{} еды.\nв Тумбочке:{} денег.\n'.format(self.fridge, self.vault))


def what_to_do(resident, room):
    random_selection = random.randint(1, 6)
    if resident.satiety < 20:
        resident.eating(room)
    elif room.fridge < 10:
        resident.shoping(room)
    elif room.vault < 50:
        resident.work(room)
    elif random_selection == 1:
        resident.work(room)
    elif random_selection == 2:
        resident.eating(room)
    else:
        resident.play()


count = 0
my_home = Home()
my_home.add_room_mate()
while True:
    count += 1
    print('{} День'.format(count))
    for index in range(len(my_home.room_mates)):
        what_to_do(my_home.room_mates[index], my_home)
        my_home.room_mates[index].status()
        if my_home.room_mates[index].death_check():
            print('{} умер от голода.'.format(my_home.room_mates[index].name))
            break
    my_home.home_status()
    if count > 364:
        print('Поздравляю вы пережили этот тяжелый год!')
        break
