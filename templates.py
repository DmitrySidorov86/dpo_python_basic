class Sandwich:
    def __str__(self):
        return 'бутерброд'


class Butter:
    def __str__(self):
        return 'Масло'


class Bread:
    def __str__(self):
        return 'Хлеб'

    def __add__(self, other):
        if isinstance(other, Butter):
            return Sandwich()


bread = Bread()
print(bread)
butter = Butter()
print(butter)
x = bread + butter
print(x)

# а так не выйдет пока не определим __add__ в Butter
z = butter + bread