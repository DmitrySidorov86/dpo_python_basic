cards_number = int(input('Введите количество видеокарт: '))
cards_list = []

for number in range(1,cards_number+1):
    cards_serial = int(input(f'{number} видеокарта: '))
    cards_list.append(cards_serial)

print(f'Старый список видеокарт: {cards_list}')

new_model = max(cards_list)
counter = 0

for i in range(len(cards_list)):
    if cards_list[i] == new_model:
        counter += 1

for _ in range(counter):
    cards_list.pop(cards_list.index(new_model))

print(f'Новый список видеокарт: {cards_list}')



