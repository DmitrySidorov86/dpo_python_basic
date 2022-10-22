def fibonachi(position):
    if position == 0:
        return 0
    if position == 1 or position == 2:
        return 1
    return fibonachi(position-1)+fibonachi(position-2)


number = int(input('Введите позицию числа в ряде Фибоначчи: '))
print('Число: {}'.format(fibonachi(number)))
