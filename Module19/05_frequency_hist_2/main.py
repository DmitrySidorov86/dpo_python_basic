text = input('Введите текст: ')
text_list = list(text)
text_dict = dict()
for symbol in text_list:
    if symbol in text_dict.keys():
        text_dict[symbol] += 1
    else:
        text_dict[symbol] = 1
print('\nОригинальный словарь частот:')
for i_keys in sorted(text_dict.keys()):
    print(i_keys,':',text_dict[i_keys])
inverted_dict = dict()
for i_value in text_dict.keys():
    if text_dict[i_value] not in inverted_dict:
        inverted_dict[text_dict[i_value]] = []
        inverted_dict[text_dict[i_value]].append(i_value)
    else:
        inverted_dict[text_dict[i_value]].append(i_value)
print('\nИнвертированный словарь частот:')
for keys in sorted(inverted_dict.keys()):
    print(keys,':',inverted_dict[keys])

