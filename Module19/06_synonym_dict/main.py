number = int(input('Введите количество пар слов: '))
even = '-'
print('\nВведите пару синонимов разделенных "-".')
synonym_dict = dict()
count = 0
while count != number :
    words = input('{0} пара: '.format(count+1))
    if even in words:
        words_list = words.split('-')
        synonym_dict[words_list[0].rstrip()] = words_list[1].lower().lstrip()
        count += 1
    else:
        print('В словах отсутствует разделитель "-"!Попробуйте ввести пару синонимов снова!')

while True:
    cheсk_word = input('Введите слово: ')
    if cheсk_word.lower() in synonym_dict.values():
        print('Синоним: {0}'.format(list(synonym_dict.keys())[list(synonym_dict.values()).index(cheсk_word)]))
    elif cheсk_word == 'end':
        break
    else:
        print('Такого слова в словаре нет.')
    