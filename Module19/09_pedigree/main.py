number = int(input('Введите количество человек: '))
family_tree = dict()
count = 0
for i_number in range(1, number):
    pair = input(f'{i_number} пара: ')
    children_list = pair.split(' ')
    if children_list[1] not in family_tree.keys():
        family_tree[children_list[1]] = 0
        family_tree[children_list[0]] = family_tree[children_list[1]] + 1
    elif children_list[1] in family_tree.keys():
        family_tree[children_list[0]] = family_tree[children_list[1]] + 1
print('\n"Высота" каждого члена семьи: ')
for i_keys in sorted(family_tree.keys()):
    print(i_keys, family_tree[i_keys] )
