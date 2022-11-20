class Water:
    def __str__(self):
        return 'Вода'

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Dirt()
        else:
            return None


class Fire:
    def __str__(self):
        return 'Огонь'

    def __add__(self, other):
        if isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Water):
            return Steam()
        elif isinstance(other, Earth):
            return Lava()
        else:
            return None


class Air:
    def __str__(self):
        return 'Воздух'

    def __add__(self, other):
        print(self)
        print(other)
        if isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Water):
            return Storm()
        elif isinstance(other, Earth):
            return Dust()
        else:
            return None


class Earth:
    def __str__(self):
        return 'Земля'

    def __add__(self, other):
        if isinstance(other, Fire):
            return Lava()
        elif isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Air):
            return Dust()
        else:
            return None


class Storm:
    def __str__(self):
        return 'Шторм'


class Dust:
    def __str__(self):
        return 'Пыль'


class Lava:
    def __str__(self):
        return 'Лава'


class Lightning:
    def __str__(self):
        return 'Молния'


class Dirt:
    def __str__(self):
        return 'Грязь'


class Steam:
    def __str__(self):
        return 'Пар'


def magick(element_1, element_2):
    result = element_1 + element_2
    return result


def choice(index):
    if index == 1:
        return air
    elif index == 2:
        return water
    elif index == 3:
        return fire
    elif index == 4:
        return earth


air = Air()
water = Water()
fire = Fire()
earth = Earth()

while True:
    question_1 = int(input('Какой первый элемент выберете(например 1)?\n1)Воздух\n2)Вода\n3)Огонь\n4)Земля\n'))
    element_one = choice(question_1)
    print('Вы выбрали {}\n'.format(element_one))
    question_2 = int(input('Какой второй элемент выберете(например 1)?\n1)Воздух\n2)Вода\n3)Огонь\n4)Земля\n'))
    element_two = choice(question_2)
    print('Вы выбрали {}\n'.format(element_two))
    print('\n{}+{}={}\n'.format(element_one, element_two, magick(element_one, element_two)))
