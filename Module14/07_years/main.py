begin = 999
end = 10000

while begin < 1000 or 1000 < end > 9999 or begin >= end:
    begin = int(input('Введите первый год(не меньше 1000): '))
    end = int(input('Введите второй год(не менее 1001 и не более 9999): '))
    if begin < 1000 or 1000 < end > 9999 or begin >= end:
        print('Вы ввели не правильный диапазон дат.')
print(f'Годы от {begin} до {end} c тремя одинаковыми цифрами:')
for number in range(begin,end+1):
    variable = list(str(number))
    variable.sort()
    if (variable[0] == variable[1] and variable[1] == variable[2]) or (variable[1] == variable[2] and variable[2] == variable[3]):
        print(number)