#Dave Gahan The BEST
violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

number = int(input('Сколько песен выбрать? '))
time = 0
special = []

for i in range(number):
    name = input(f'Название {i+1} песни: ')
    for i_treck in violator_songs:
        if i_treck[0] == name:
            time += i_treck[1]
            special.append(i_treck)

print(f'Общее время звучания песен: {round(time,2)}.')

