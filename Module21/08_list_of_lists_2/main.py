def opening(list_uno):
    new_list = []
    for element in list_uno:
        if isinstance(element, list):
            new_list += opening(element)
        else:
            new_list.append(element)
    return new_list


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

list_one = opening(nice_list)

print(list_one)
