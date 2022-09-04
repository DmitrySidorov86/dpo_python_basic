cell_number = int(input('Введите количество клеток: '))
cell_list = []
defective_list = []

for number in range(1,cell_number+1):
    cell_effect = int(input(f'эффективность {number} клетки: '))
    cell_list.append(cell_effect)
    if number > cell_effect:
        defective_list.append(cell_effect)

print(f'Неподходящие значения: {", ".join([str(i) for i in defective_list])}.')
