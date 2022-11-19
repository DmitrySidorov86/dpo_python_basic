class Gardener:
    def __init__(self):
        self.name = input('Как зовут садовника? \n')
        self.working_bed = PotatoGarden()

    def harvest(self):
        if worker.working_bed.are_all_ripe():
            self.working_bed.potatoes = list()
            print('Урожай собран')
        else:
            print('Урожай не созрел!')

    def plant_garden(self):
        if len(self.working_bed.potatoes) == 0:
            self.working_bed = PotatoGarden(int(input('Сколько картошки хотите посадить')))
        else:
            print('Вы не собрали предыдущий урожай')

    def info(self):
        print('Имя садовника:\n{}'.format(self.name))
        if len(self.working_bed.potatoes) == 0:
            print('Грядка пуска')
        else:
            print('На грядке растет {} кустов {}.'.format(len(self.working_bed.potatoes), 'картошки'))
            self.working_bed.print_all_states()


class PotatoGarden:
    def __init__(self, index=5):
        self.potatoes = [Potato(index) for index in range(1, index + 1)]

    def grow_all(self):
        if len(self.potatoes) != 0:
            print('Картошка прорастает!')
            for potato in self.potatoes:
                potato.grow()

    def are_all_ripe(self):
        for potato in self.potatoes:
            if not potato.is_ripe():
                return False
        else:
            return True

    def print_all_states(self):
        for potato in self.potatoes:
            potato.print_state()


class Potato:
    states = {0: 'Отсутствует', 1: 'Росток', 2: 'Зеленая', 3: 'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def print_state(self):
        print('Картошка {} сейчас {}'.format(
            self.index, Potato.states[self.state]))


worker = Gardener()
worker.info()

while True:
    worker.working_bed.grow_all()
    worker.working_bed.are_all_ripe()
    print('Выберите действие(1/2):')
    while True:
        question = int(input('1)Убрать урожай\n2)Посадить урожай\n'))
        if question == 1:
            worker.harvest()
            break
        elif question == 2:
            worker.plant_garden()

            break
        else:
            print('Так что делать садовнику(1/2):')
