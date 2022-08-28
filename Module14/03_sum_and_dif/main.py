def summ (numeral):
    numeral_summ = 0
    while numeral != 0:
        numeral_summ += numeral % 10
        numeral //= 10
    numeral_summ += numeral
    return numeral_summ

def amount (numeral):
    count = 0
    while numeral != 0:
        count += 1
        numeral //= 10
    return count

number = int(input('Введите число:'))

print(f'\nСумма чисел:{summ(number)}')
print(f'Количество цифр в числе:{amount(number)}')
difference = summ(number) - amount(number)
print(f'\nРазность суммы и количества цифр:{difference}')

