def number_coutn(i_list):
    count = sum(map(lambda x: 1 if x.isdigit() else 0, i_list))
    return count


while True:
    password = input('Придумайте пароль: ')
    if len(password) < 8 or password.islower() or number_coutn(password) < 3:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
    else:
        print('Это надёжный пароль!')
        break
