class Potato:
    stage = {0: 'Посажена', 1: 'Росток', 2: 'Зеленая', 3: 'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.stage = 0

    def grow_potato(self):
        if self.stage != 3:
            self.stage += 1
        self.print_potato()

    def print_potato(self):
        print('Potato {} is {}'.format(self.index, Potato.stage[self.stage]))

    def ripe_potato(self):
        if self.stage == 3:
            return True
        else:
            return False


class Garden:
    def __init__(self, count):
        self.garden = [Potato(index) for index in range(1, count + 1)]

    def garden_grow(self):
        for potato in self.garden:
            potato.grow_potato()

    def cheсk_ripe(self):
        if not all([potatos.ripe_potato() for potatos in self.garden]):
            print('Potatos not ripe')
        else:
            print('Potatos ripe')

    def print_garden(self):
        print(self.garden)


number = int(input('?:'))
garden_1 = Garden(number)
for _ in range (3):
    garden_1.garden_grow()
    garden_1.cheсk_ripe()
