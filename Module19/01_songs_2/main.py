violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}
number = int(input('Сколько песен выбрать ?'))
time = []
for i in range(1,number+1):
     song = input(f'Название {i} песни:')
     time.append(violator_songs[song])
print(f'Общее время звучания песен: {round(sum(time),2)} минуты.')
