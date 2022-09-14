number = int(input('Введите длинну списка: '))
number_list = [1 if x % 2 == 0 else x % 5 for x in range(number)]

print(f'Результат: {number_list}')

