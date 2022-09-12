guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:

    print(f'\nСейчас на вечеринке {len(guests)} человек: {",".join(guests)}.')
    greetings = input('Гость пришёл или ушёл? ')

    if greetings == 'Пора спать':
        print('Вечеринка закончилась, все легли спать.')
        break

    guest_name = input('Имя гостя: ')

    if greetings == 'пришёл' :

        if len(guests) != 6:
            guests.append(guest_name)
            print(f'Привет, {guest_name}')

        else:
            print(f'Прости, {guest_name}, но мест нет!')

    if greetings == 'ушёл':
        print(f'Пока, {guest_name}')
        guests.remove(guest_name)

