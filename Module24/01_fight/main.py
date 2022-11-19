import random


class Unit:
    def __init__(self, number, heals=100):
        self.number = number
        self.heals = heals

    def lose_heals(self):
        self.heals -= 20

    def print_unit_status(self):
        print('{} Warrior take 20 dammage, {} heals left.\n'.format(self.number, self.heals))

    def death_check(self):
        if self.heals == 0:
            print('The {} Warrior died!'.format(self.number))
            return True
        else:
            return False


class Battle:
    def __init__(self):
        self.pare_of_warriors = [Unit(number) for number in range(1, 3)]

    def print_dict(self):
        print('{}'.format(self.pare_of_warriors))

    def warriors_battle(self):
        warrior_number = random.randint(0, 1)
        if warrior_number == 0:
            print('The second warrior attacked the first warrior! ')
        else:
            print('The first warrior attacked the second warrior! ')
        self.pare_of_warriors[warrior_number].lose_heals()
        self.pare_of_warriors[warrior_number].print_unit_status()
        if self.pare_of_warriors[warrior_number].death_check():
            return True
        else:
            return False


versus = Battle()

while True:
    if versus.warriors_battle():
        break
