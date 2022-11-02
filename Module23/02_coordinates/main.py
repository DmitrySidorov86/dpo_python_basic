import random


def random_number():
    x = random.randint(0, 100)
    return x


def f(x, y):
    try:
        x += random.randint(0, 10)
        y += random.randint(0, 5)
        z = round(x / y, 2)
    except ZeroDivisionError:
        print('На 0 делить нельзя')
    return z


def f2(x, y):
    try:
        x -= random.randint(0, 10)
        y -= random.randint(0, 5)
        z = round(y / x, 2)
    except ZeroDivisionError:
        print('На 0 делить нельзя')
    return z


couple_number = int(input('Сколько пар чисел будет в файле?'))
with open('coordinates.txt', 'w', encoding='utf8') as file_one:
    for _ in range(0, couple_number):
        line = str(random_number())+' '+str(random_number())+'\n'
        file_one.write(line)

file_2 = open('result.txt', 'w')
file_2.close()
file = open('coordinates.txt', 'r')

try:
    for line in file:
        line.strip('\n')
        nums_list = line.split()
        res1 = f(int(nums_list[0]), int(nums_list[1]))
        res2 = f2(int(nums_list[0]), int(nums_list[1]))
        number = random.randint(0, 100)
        file_2 = open('result.txt', 'a')
        my_list = sorted([res1, res2, number])
        my_list = [str(x) for x in my_list]
        file_2.write(' '.join(my_list)+'\n')
    file.close()
    file_2.close()
except ValueError as error:
    print('Нельзя просто так взять и закрыть то что не открывали')
