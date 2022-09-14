def change(x):
    for letter in alphabet:
        if x == letter:
            return alphabet[alphabet.index(x)%alphabet.index(x)+code]


alphabet = 'абвгдеёжзиклмнопрстуфхцчшщъыьэюя'
text = input('Введите сообщение: ')
code = int(input('Введите сдвиг: '))
code_list = [change(x) if x in alphabet else " " for x in text ]

print(f'Зашифрованное сообщение: {"".join(code_list)}')



