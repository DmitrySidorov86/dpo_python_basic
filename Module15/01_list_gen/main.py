number_list = [1]
end_number = int(input('Введите число: '))

for i in range(end_number):
    number_list.append(number_list[i]+2)
    if number_list[i] + 2 > end_number:
        if number_list[-1] > end_number:
            number_list.pop()
        break

print(number_list)