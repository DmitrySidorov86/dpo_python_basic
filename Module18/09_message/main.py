text = input('Сообщение:')
word = []
new_text_list = ''
secret_list = []
for i in text:
    number = text.index(i)
    if text.index(i) == len(text):
        word.append(i)
        word.reverse()
        new_text_list += ''.join(word)
    elif i != ' ':
        if i.isalpha():
            word.append(i)
            secret_list = word.copy()
        else:
            word.reverse()
            word.append(i)
            new_text_list += ''.join(word)
            word = []
    elif i == ' ':
        word.reverse()
        word.append(' ')
        new_text_list += ''.join(word)
        word = []
if not text.endswith(('!','"','"','#','$','%','&','(',')','*','+',',','-','.','/',':',';','<','=','>','?','@',"'",' '
                         ,'[',"\\",']','^','_','`','{','|','}','~')):
    secret_list.reverse()
    new_text_list += ''.join(secret_list)

print(f'Новое сообщение: {new_text_list}')
