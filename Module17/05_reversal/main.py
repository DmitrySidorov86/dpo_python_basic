text = input('Введите строку: ')
text_list = list(text)
del text_list [:text_list.index('h')+1]
text_list.reverse()
del text_list [:text_list.index('h')+1]

print(f'Развёрнутая последовательность между первым и последним h: {"".join(text_list)}')


