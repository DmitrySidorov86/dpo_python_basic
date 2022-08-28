def werewolf(numeral):
    text_numeral = str(numeral)
    before , after = text_numeral.split('.')
    even_one = list(before)
    even_one.reverse()
    new_before = ''.join(even_one)
    even_two = list(after)
    even_two.reverse()
    new_after = ''.join(even_two)
    new_number = float(f'{new_before}.{new_after}')
    return new_number

number_one = float(input('Введите первое число: '))
number_two = float(input('Введите второе число: '))
revers_one = werewolf(number_one)
revers_two = werewolf(number_two)
print(f'\nПервое число наоборот:{revers_one}')
print(f'Второе число наоборот:{revers_one}')
print(f'\nСумма:{revers_one + revers_two}')

