def palindrom_check(list):
    for i in range(round(len(list) / 2)):
        if list[i] != list[-1 - i]:
            return False
    return True

numbers = int(input('Кол-во чисел: '))
number_list =[]

for _ in range(numbers):
    numeral = int(input('Число: '))
    number_list.append(numeral)

variable = palindrom_check(number_list)
count_number = 1

if variable == True:
    print(f'\nПоследовательность: {number_list}')
    print(f'Нужно приписать чисел: 0')
    print(f'Сами числа:_____')

while variable == False:

    new_list = []
    check_list = number_list.copy()

    for _ in range(count_number):
        new_list.append(check_list[_])
    new_list.reverse()
    check_list += new_list
    count_number += 1

    if palindrom_check(check_list) == True:
        print(f'\nПоследовательность: {number_list}')
        print(f'Нужно приписать чисел: {len(new_list)}')
        print(f'Сами числа{new_list}')
        break
