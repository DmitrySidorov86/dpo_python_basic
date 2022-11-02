import random


def show_file(file_name):
    with open(file_name, 'r') as file_open:
        for line in file_open:
            print(line.strip('\n'))


def write_in_file(file_name, text):
    with open(file_name, 'a') as file_open:
        insert_text = str(text) + '\n'
        file_open.write(insert_text)


clean_file = open('out_file.txt', 'w')
clean_file.close()
number_summ = 0
random_list = [x for x in range(1, 13)]
while number_summ < 777:
    number = int(input('Введите число:'))
    if random.choice(random_list) == 3:
        print('Вас постигла неудача')
        print('\nСодержимое файла out_file.txt:')
        show_file('out_file.txt')
        raise BaseException
    else:
        number_summ += number
        write_in_file('out_file.txt', number)

print('Вы успешно выполнили условие для выхода из порочного цикла!')
print('\nСодержимое файла out_file.txt:')
show_file('out_file.txt')
