text = input('Введите строку: ')
text_list = list(text)
variable = 1
new_list = []

for i in range(len(text_list)+1):

    if i < len(text_list)-1:

        if text_list[i] == text_list[i + 1]:
            variable += 1

        else:
            new_list.append(text_list[i])
            new_list.append(str(variable))
            variable = 1

    else:

        if text_list[i] == text_list[-1]:
            new_list.append(text_list[i])
            new_list.append(str(variable))

        else:

            new_list.append(text_list[-1])
            new_list.append(str(1))

        break

print(''.join(new_list))




