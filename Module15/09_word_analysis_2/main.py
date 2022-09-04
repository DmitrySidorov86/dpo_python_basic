word = input('Введите слово: ')
word_list = list(word)
counter = 0
palindrom = 1
for i in range(round(len(word_list) / 2)):
    if word_list[i] == word_list[-1-counter]:
        counter += 1
    else:
        palindrom = 0
        break
if palindrom == 1 :
    print('Это Палиндром!')
else:
    print('Это Не Палиндром!')

