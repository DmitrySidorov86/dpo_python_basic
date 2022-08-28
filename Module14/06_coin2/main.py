import math
def search(x,y):
    distance = math.sqrt(x**2+y**2)
    return distance
while True:
    print('Введите координаты монетки:')
    width = float(input('X: '))
    height = float(input('Y: '))
    area = float(input('Введите радиус:'))
    if area >= search(width,height):
        print('Монетка где-то рядом')
        break
    else:
        print('Монетки в области нет')
