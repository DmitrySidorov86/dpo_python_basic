number = int(input('Введите длинну списка: '))
number_list = []

for _ in range(number):
    variable = input('Введите элемент списка: ')
    number_list.append(variable)

print(f'Список:{number_list}')

new_list = sorted(number_list)  # или number_list.sort()

print((f'Отсортированный список:{new_list}'))#print((f'Отсортированный список:{number_list}'))
