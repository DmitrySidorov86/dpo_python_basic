alphabet = 'qwertyuiopasdfghjklzxcvbnm'
file_open = open('zen.txt', 'r')
word_number = 0
line_number = 0
letter_number = 0
letter_dict = dict()

for line in file_open:
    line_number += 1
    line_list = line.split(' ')
    word_number += len(line_list)
    for word in line_list:
        for symbol in word:
            if symbol.lower() in alphabet:
                 letter_number += 1
                 if symbol.lower() not in letter_dict.keys():
                     letter_dict[symbol.lower()] = 1
                 else:
                     letter_dict[symbol.lower()] += 1

print(f'Количество букв в файле: {letter_number}')
print(f'Количество слов в файле: {word_number}')
print(f'Количество строк в файле: {line_number}')
lowwest_letter = [x for x, y in letter_dict.items() if y == min(letter_dict.values())][0]
print(f'Наиболее редкая буква: {lowwest_letter}')
