import random

number = int(input('Количество чисел в списке: '))
number_list = [random.randint(0,2) for _ in range (number) ]

print(f'\nСписок до сжатия: {number_list}')

for i_list in number_list:
    if i_list == 0:
        number_list.insert(number,i_list)
        number_list.remove(i_list)

del number_list[-number_list.count(0):]

print(f'Список после сжатия: {number_list}')