word = input('Введите слово: ')
word_list = list(word)
counter = 0
palindrom = True
for i in range(round(len(word_list) / 2)):
    if word_list[i] == word_list[-1-counter]:
        counter += 1
    else:
        palindrom = False
        break
if palindrom == True :
    print('Это Палиндром!')
else:
    print('Это Не Палиндром!')

