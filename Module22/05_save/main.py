import os


def save_path():
    path_list = input('Куда хотите сохранить документ? Введите последовательность папок (через пробел):\n').split(' ')
    way = os.path.abspath(os.path.join(os.path.sep))
    for i in range(len(path_list)):
        way = adress(way, path_list[i])
    return way


def adress(path, element):
    file_adress = os.path.join(path, element)
    return file_adress


def write(path, message):
    file = open(path, 'w', encoding='utf8')
    file.write(message)
    file.close()


text = input('Введите строку: ')
core_way = save_path()

while True:
    if not os.path.exists(core_way):
        print('Данного пути не существует')
        core_way = save_path()
    else:
        break

file_name = input('Введите имя файла:') + '.txt'
core_way = os.path.join(core_way, file_name)
if os.path.exists(core_way):
    question = input('Вы действительно хотите перезаписать файл?').lower()
    while True:
        if question == 'да':
            write(core_way, text)
            print('Файл успешно перезаписан!')
            break
        else:
            question = input('Может все таки перезапишем?').lower()
else:
    write(core_way, text)
    print('Файл успешно сохранён!')
