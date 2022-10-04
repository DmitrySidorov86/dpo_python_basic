search = input('Введите фамилию:').lower()
data = {'Сидоров Никита': 35, 'Сидорова Алина': 34, 'Сидоров Павел': 10, 'Иванов Иван': 14, 'Иванова Ирина': 25,
        'Петрова Валентина': 40}
for name, age in data.items():
    if name.lower().startswith(search):
        print(f'{name} {age}')
