telephone_book = dict()

while True:
    request = int(input('Введите номер действия:\n\t1. Добавить контакт\n\t2. Найти человека\n'))
    if request == 1:
        name, surname = input('Введите имя и фамилию нового контакта (через пробел): ').split(' ')
        if (name, surname) in telephone_book:
            print('Такой человек уже есть в контактах.')
        else:
            telephone_number = input('Введите номер телефона: ')
            telephone_book[(name, surname)] = telephone_number
        print(f'Текущий словарь контактов: {telephone_book}')
    elif request == 2:
        search = input('Введите фамилию для поиска: ')
        for info, number in telephone_book.items():
            if search.capitalize() in info:
                print(info, number)
