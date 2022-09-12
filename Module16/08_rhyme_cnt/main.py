def census(list):
    print(f'\nТекущий круг людей: {list}')
    start_number = int(input('Начало счёта с номера: '))
    return start_number

def delete(variable):
    print(f'Выбывает человек под номером {man_list[variable]}')
    man_list.pop(variable)
    return man_list


number = int(input('Кол-во человек: '))
counting = int(input('Какое число в считалке? '))
print(f'Значит выбывает каждый {counting}-й игрок!')
man_list = list(range(1, number + 1))
begin_number = census(man_list)
counter = counting

while True:

    if begin_number in man_list:

        if counter >= len(man_list) - man_list.index(begin_number):
            counter -= len(man_list) - man_list.index(begin_number)

            while counter >= len(man_list):
                counter -= len(man_list)
            delete(counter - 1)
            begin_number = census(man_list)
            counter = counting

        elif counter < len(man_list) - man_list.index(begin_number):
            delete(man_list.index(begin_number) + counter - 1)
            begin_number = census(man_list)
            counter = counting

        if len(man_list) == 1:
            print(f'\nОстался человек под номером {man_list[0]}')
            break

    else:
        print(f'Игрока с номером {begin_number} нет среди участников.\n'
              f'Попробуйте еще раз!')
        begin_number = census(man_list)
