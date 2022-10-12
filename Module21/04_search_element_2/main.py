site = {'html': {
                'head': {
                    'title': 'Мой сайт'
                },
                'body': {
                    'h2': 'Здесь будет мой заголовок',
                    'div': 'Тут, наверное, какой-то блок',
                    'p': 'А вот здесь новый абзац'}
             }
        }


def search(dict_one, keyword, deep=3):
    count = 0
    if keyword in dict_one.keys():
        return dict_one[keyword]
    else:
        for key, value in dict_one.items():
            if isinstance(value, dict):
                count += 1
                if count == deep:
                    return None
                result = search(value, keyword, deep)
                if result:
                    return result


question = input('Введите искомый ключ: ')
question_deep = input('Хотите ввести максимальную глубину? Y/N: ').lower()
if question_deep == 'y':
    max_deep = int(input('Введите максимальную глубину:'))
    answer = search(site, question, deep=max_deep)
else:
    answer = search(site, question,)

print(answer)
