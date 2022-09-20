forbidden_simbol_list = '@№$%^&\*()'
file_name = input('Название файла: ')
for i in forbidden_simbol_list:
    if file_name.startswith(i):
        print('Ошибка: название начинается на один из специальных символов.')
        break
if not file_name.endswith('.txt') or file_name.endswith('.docx'):
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')
else:
    print('Файл назван верно')
