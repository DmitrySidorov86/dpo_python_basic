import datetime


def write_file(name_list):  # заполнение файла именами
    with open("people.txt", 'w', encoding='utf8') as file_open:
        for element in name_list:
            text = element + '\n'
            file_open.write(text)


def errors_log(error):
    with open("errors.log", 'a', encoding='utf8') as file_open:
        errors_text = str(datetime.datetime.now()) + ':' + error + '\n'
        file_open.write(errors_text)


while True:
    first_question = input('Вы хотите  использовать свой список имен, или воспользуетесь шаблонным списком(да/нет): '
                           '').lower()
    if first_question != 'да' and first_question != 'нет':
        print('Так вы введете свой список имен ("да"), или воспользуетесь шаблоном ("нет") ?')
    else:
        break

user_name_list = list()
example_list = ['Василий', 'Николай', 'Надежда', 'Никита', 'Ян', 'Ольга', 'Евгений', 'Кристина']

if first_question == 'да':
    name_number = int(input('Сколько имен вы хотите внести?\n'))
    for i in range(1, name_number + 1):
        user_name_list.append(input(f'Ведите {i}-е имя :'))
elif first_question == 'нет':
    user_name_list = list.copy(example_list)
write_file(user_name_list)
letter_sum = 0
counter = 1
number_list = list()
with open("people.txt", 'r', encoding='utf8') as file:
    for line in file:
        name_line = line.strip('\n')
        try:
            letter_num = len(name_line)
            if letter_num < 3:
                errors_log(f'Ошибка : менее трех символов в строке {str(counter)}')
                raise Exception()
        except Exception:
            print(f'Ошибка : менее трех символов в строке {str(counter)}')
        else:
            letter_sum += len(name_line)
            number_list.append(len(name_line))
        counter += 1
print(f'Общее количество символов:{letter_sum}.')
