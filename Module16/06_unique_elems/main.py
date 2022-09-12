first = []
second =[]
for i in range(3):
    number=int(input(f'Введите {i+1}-е число для первого списка: '))
    first.append(number)
for i in range(7):
    number = int(input(f'Введите {i + 1}-е число для первого списка: '))
    second.append(number)
print(f'Первый список:{first}')
print(f'Второй список:{second}')
first += second
for i in first:
    while first.count(i) > 1:
        first.remove(i)
print(first)