def search(x):
    answer = [i_country  for i_country in country_dict if x in country_dict[i_country]]
    return answer

number = int(input('Колисчество стран: '))
country_dict = dict()
for i in range(1,number+1):
    text = input(f'{i} страна: ')
    country = text.split(' ')
    country_dict[country[0]] = country[1:]
for i in range(1,4):
    question = input(f'\n{i} город: ')
    if search(question) != []:
        print(f'Город {question} расположен в стране {"".join(search(question))}')
    else:
        print(f'По городу {question} нет данных!')