def census(list_one):
    if counter > len(list_one):
        start_number = counter % len(list_one)
    elif counter == 0:
        start_number = counter
    else:
        start_number = counter-1
    return start_number


def delete(variable):
    print(f'Выбывает человек под номером {man_list[variable]}')
    man_list.pop(variable)
    return man_list


number = int(input('Кол-во человек: '))
counting = int(input('Какое число в считалке? '))
print(f'Значит выбывает каждый {counting}-й игрок!')
man_list = list(range(1, number + 1))
begin_number = 0
counter = counting

if len(man_list) == 1:
    print(f'\nОстался человек под номером {man_list[0]}')
else:
    while True:

        if man_list[begin_number] in man_list:
            print(f'\nТекущий круг людей: {man_list}')
            print(f'Начало счёта с номера:{man_list[begin_number]} ')
            if counter >= len(man_list[begin_number:]):
                counter -= len(man_list[begin_number:])
                counter %= len(man_list)
                delete(counter - 1)
                if len(man_list) == 1:
                    print(f'\nОстался человек под номером {man_list[0]}')
                    break
                else:
                    begin_number = census(man_list)
                    counter = counting

            elif counter < len(man_list[begin_number:]):
                delete(begin_number + counter - 1)
                if len(man_list) == 1:
                    print(f'\nОстался человек под номером {man_list[0]}')
                    break
                begin_number = census(man_list)
                counter = counting
        else:
            print(f'Игрока с номером {begin_number} нет среди участников.\n'
                  f'Попробуйте еще раз!')
            begin_number = census(man_list)
