import os


def size(way):
    size_list = []
    dir_list = []
    try:
        for element in os.listdir(way):
            if os.path.isfile(os.path.join(way, element)):
                size_list.append(os.path.getsize(os.path.join(way, element)))
            elif os.path.isdir(os.path.join(way, element)):
                dir_list.append(1)
                result, dir_number = size(os.path.join(way, element))
                dir_list.extend(dir_number)
                if result:
                    size_list.extend(result)
    except PermissionError as e:
        item = 1
    return size_list, dir_list


path = os.path.abspath(os.path.join('..', '..', '..'))
file_list, dir_list_one = size(path)
print(path)
print(f'Размер каталога (в КБ): {sum(file_list)/1024}')
print(f'Количество файлов: {len(file_list)}')
print(f'Количество подкаталогов: {len(dir_list_one)}')
