number = int(input('Введите длинну списка: '))
number_list = []
for _ in range(number):
    variable = input('Введите элемент списка: ')
    number_list.append(variable)
step = int(input('На сколько надо подвинуть бегущую строку ? '))
for shift in range(1,step+1):
    number_list += number_list.pop(0)
    print(f'{shift} смещение{number_list}')


