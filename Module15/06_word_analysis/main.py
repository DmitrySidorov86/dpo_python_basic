word = input('Введите слово: ')
word_list = list(word)
word_simbol = len(word_list)
uniq_simbol = 0
for i in range(word_simbol):
    if int(word_list.count(word_list[i])) == 1:
        uniq_simbol += 1
print(f'Количество уникальных букв: {uniq_simbol} .')

