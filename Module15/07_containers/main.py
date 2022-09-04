conteners_number = int(input('Введите количество контейнеров: '))
conteners_list = [200]
counter = 0

while counter != conteners_number:
    weight = int(input('Введите вес контейнера: '))
    if weight > conteners_list[counter] or weight > 200:
        print('Вы ввели неверный вес. Напоминаю!\nВес контейнера не должен превышать 200 кг , так же он не должен превышать вес предыдущего контейнера!\nПопробуйте снова!')
    elif weight <= conteners_list[counter] :
        conteners_list.append(weight)
        counter += 1

conteners_list.pop(0)

while True:
    new_contener_weigth = int(input('Введите вес нового контейнера: '))
    if new_contener_weigth > 200:
        print('Вы ввели неверный вес. Напоминаю!\nВес контейнера не должен превышать 200 кг.')
    else:
        break

position = 0

for a in range(conteners_number):
    if new_contener_weigth <= conteners_list[a]:
        position = a + 2
    elif new_contener_weigth > conteners_list[a]:
        break

print(f'Место нового контейнера под номером {position}.')


