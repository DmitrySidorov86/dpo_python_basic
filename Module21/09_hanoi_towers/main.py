def move(number, fromm, were):
    if number == 1:
        print(f'Переложить диск {number} со стержня номер {fromm} на стержень номер {were}')
        return
    move(number-1, fromm, 6-fromm-were)
    print(f'Переложить диск {number} со стержня номер {fromm} на стержень номер {were}')
    move(number-1, 6-fromm-were, were)


disc_number = int(input('Введите количество дисков: '))
move(disc_number, 1, 3)


