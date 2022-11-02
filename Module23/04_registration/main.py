def write_in_file(file_name, text):
    with open(file_name, 'a', encoding='utf8') as file_open:
        insert_text = str(text) + '\n'
        file_open.write(insert_text)


clean_file_one = open('registrations_good.log', 'w')
clean_file_one.close()
clean_file = open('registrations_bad.log', 'w')
clean_file.close()
age_list = [x for x in range(10, 99)]
with open('registrations.txt', 'r', encoding='utf8') as file_open:
    for line in file_open:
        line_list = line.split(' ')
        try:
            if len(line_list) != 3:
                raise IndexError('НЕ присутствуют все три поля')
            elif len(line_list) == 3:
                for letter in line_list[0]:
                    if not letter.isalpha():
                        raise NameError('Поле «Имя» содержит НЕ только буквы')
                if '@' not in line_list[1] and '.' not in line_list[1]:
                    raise SyntaxError('Поле «Имейл» НЕ содержит @ и . (точку)')
                if int(line_list[2]) not in age_list:
                    raise ValueError('Поле «Возраст» НЕ является числом от 10 до 99')
        except IndexError as index_log:
            message = line.strip('\n') + '\t'*3 + str(index_log)
            write_in_file('registrations_bad.log', message)
        except NameError as name_log:
            message = line.strip('\n') + '\t' * 3 + str(name_log)
            write_in_file('registrations_bad.log', message)
        except SyntaxError as syntax_log:
            message = line.strip('\n') + '\t' * 3 + str(syntax_log)
            write_in_file('registrations_bad.log', message)
        except ValueError as value_log:
            message = line.strip('\n') + '\t' * 3 + str(value_log)
            write_in_file('registrations_bad.log', message)
        else:
            write_in_file('registrations_good.log', line.strip('\n'))
