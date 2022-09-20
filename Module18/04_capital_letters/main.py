text = input('Введите строку: ')
text_list = text.split()
new_list = []
for i in text_list:
    i = i.capitalize()
    new_list.append(i)
print(' '.join(new_list))
