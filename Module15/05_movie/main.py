film_list = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']

films_number = int(input('Какое количество фильмов хотите добавить? '))
my_film_list = []

for _ in range(films_number):
    film = input('Какой фильм хотите добавить? \n')
    if film in film_list:
        my_film_list.append(film)
    else:
        print('К сожалению в базе нет такого Фильма.Попробуйте найти другой.')

print(f'Ваш список фильмов:{", ".join(my_film_list)}.')

