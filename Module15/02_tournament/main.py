def even(name_list):
    new_name_list =[]
    for i in range (0,len(name_list),2):
        new_name_list.append(name_list[i])
    return new_name_list

champion_list = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя']

print(f'Первый день соревнований {even(champion_list)}')

