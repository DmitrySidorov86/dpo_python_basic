def zipp(*args):
    length = min(len(element) for element in args)  # максимальное кол-во кортежей
    new_list = [[item for index, item in enumerate(element) if index < length]for element in args]
    # приведение различных типов  полученных данных к одному виду.
    # для каждого element'a из аргументов создается список.
    list_two = [[new_list[second_index][first_index] for second_index in range(len(new_list))]
                for first_index in range(length)]  # range(length) - кол-во кортежей,
    # len(new_list) - кол-во эл-ов кортежа,
    # new_list[second_index][first_index] элемент списка  получается из индексов,
    # где индекс первого уровня [second_index] показывает из какого списка  берем переменную,
    # а индекс второго уровня [first_index] показывает какой элемент списка берем.
    tuple_list = [tuple(list_two[index]) for index in range(length)]
    print(tuple_list)


#a = [{"x": 4}, "b", "z", "d"]

#b = (10, {20,}, [30], "z")
a = [1, 2, 3, 4, 5]

b = {1: "s", 2: "q", 3: 4}

x = (1, 2, 3, 4, 5)

zipp(a, b, x)
