def errors_algorint(string):
    while True:
        question = input(f'Обнаружена ошибка в строке:{string} Хотите исправить (да/нет)?').lower()
        if question == 'нет':
            string = 0
            return string
        elif question == 'да':
            string = input('Введите исправленную строку: ')
            return string
        else:
            print('Так вы точно хотите исправить строку(да/нет)?')


def calc(arguments, list_symbols):
    arguments_list = arguments.split(' ')
    result = 0
    if arguments_list[1] == list_symbols[0]:
        result = int(arguments_list[0]) * int(arguments_list[2])
    elif arguments_list[1] == list_symbols[1]:
        result = int(arguments_list[0]) ** int(arguments_list[2])
    elif arguments_list[1] == list_symbols[2]:
        result = int(arguments_list[0]) + int(arguments_list[2])
    elif arguments_list[1] == list_symbols[3]:
        result = int(arguments_list[0]) - int(arguments_list[2])
    elif arguments_list[1] == list_symbols[4]:
        result = int(arguments_list[0]) // int(arguments_list[2])
    elif arguments_list[1] == list_symbols[5]:
        result = int(arguments_list[0]) / int(arguments_list[2])
    elif arguments_list[1] == list_symbols[6]:
        result = int(arguments_list[0]) % int(arguments_list[2])
    return result


symbol_list = ['*', '**', '+', '-', '//', '/', '%']
answer_summ = 0
with open('calc.txt', 'r') as calc_open:
    for line in calc_open:
        line = line.strip('\n')
        line_list = line.split(' ')
        try:
            if line_list[1] not in symbol_list:
                raise SyntaxError('Неверный знак действия')
            if line_list[0].isdigit() is False or line_list[2].isdigit() is False:
                raise ValueError('Один или оба аргумента не являются числами.')
        except SyntaxError as errors:
            line = errors_algorint(line)
        except ValueError as value_error:
            line = errors_algorint(line)
        finally:
            if line != 0:
                answer_summ += calc(line, symbol_list)
print(f'\nСумма результатов: {answer_summ}')
