def number_list(num):
    if num != 1:
        number_list(num-1)
    print(num)


number = int(input('Введите число:'))
number_list(number)
