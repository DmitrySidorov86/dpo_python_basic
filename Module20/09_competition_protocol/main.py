number = int(input('Сколько записей вносится в протокол? '))
print('Записи (результат и имя):')
prize_dict = {1: ['', 0], 2: ['', 0], 3: ['', 0]}

for approach in range(1, number + 1):
    points, name = input(f'{approach}-я запись: ').split(' ')

    if int(points) > prize_dict[1][1]:
        prize_dict[1] = [name, int(points)]

    elif (int(points) <= prize_dict[1][1]) and (int(points) > prize_dict[2][1]):
        prize_dict[2] = [name, int(points)]

    elif (int(points) <= prize_dict[2][1]) and (int(points) > prize_dict[3][1]):
        prize_dict[3] = [name, int(points)]

print('\nИтоги соревнований:')

for place, info in prize_dict.items():
    print(f'{place}-е место. {info[0]} ({info[1]})')
