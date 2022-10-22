def print_answer(file_name):
    print(f'Содержимое файла {file_name}:')
    file_open = open(file_name, 'r')
    for line in file_open:
        print(line, end='')
    file_open.close()
    print()


text_file = open('text.txt', 'w')
alphabet = 'abcdefghijklmnopqrstuvwxyz'
symbols = '!"#$%&"()*+,-./:;<=>?@[\]^_`{|}~ '

while True:
    text = input('Введите текст для анализа(на англ. языке): ')
    if text[0].lower() not in alphabet and text[0].lower() != ' ':
        print('Не весь текст введен английскими буквами..Попробуй еще разок.')
    else:
        break

text_file.write(text)
text_file.close()
text_file = open('text.txt', 'r')
analysis_dict = dict()

for string in text_file:
    for element in string:
        if element not in symbols and element.lower() in alphabet:
            if element.lower() not in analysis_dict.keys():
                analysis_dict[element.lower()] = 1
            else:
                analysis_dict[element.lower()] += 1

text_file.close()
all_letters = sum(analysis_dict.values())
new_analysis_dict = dict()

for keys, values in analysis_dict.items():
    letter_ratio = round(values/all_letters, 3)
    if letter_ratio not in new_analysis_dict.keys():
        new_analysis_dict[letter_ratio] = keys
    else:
        new_analysis_dict[letter_ratio] += keys

for keys, values in new_analysis_dict.items():
    new_analysis_dict[keys] = sorted(values)

new_analysis_dict = dict(sorted(new_analysis_dict.items(), key=lambda x: x[0], reverse=True))
analysis_file = open('analysis.txt', 'w')

for keys, values in new_analysis_dict.items():
    for element in values:
        answer = element + ' ' + str(keys) + '\n'
        analysis_file.write(answer)

analysis_file.close()
print_answer('text.txt')
print_answer('analysis.txt')
