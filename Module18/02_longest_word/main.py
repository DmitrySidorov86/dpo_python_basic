text = input('Введите строку: ')
text_list = text.split()[:]
maxx = 0
word = ''

for i in text_list:
    if len(i) > maxx:
        maxx = len(i)
        word = i

print('\nСамое длинное слово: {max_word}'.format(
    max_word=word)
)
print('Длина этого слова: {max_count}'.format(
    max_count=maxx)
)