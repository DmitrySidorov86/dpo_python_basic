def minn (numeral):
    min_divider = numeral
    for i in range(2,numeral+1):
        if numeral % i == 0:
            if min_divider > i:
                min_divider = i

    return min_divider

number = int(input('Введите число: '))
print(f'Наименьший делитель, отличный от единицы:{minn(number)}')
