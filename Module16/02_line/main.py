firstclass_list = list(range(160,177,2))
secondclass_list = list(range(162,181,3))
firstclass_list.extend(secondclass_list)
firstclass_list.sort()
print(f'Отсортированный список учеников:{firstclass_list}')

