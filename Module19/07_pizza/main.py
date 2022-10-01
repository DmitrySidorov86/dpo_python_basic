
number_of_order = int(input('Введите количество заказов: '))
main_order_dict = dict()
print('Вводите заказ через пробел(Имя Пицца Количество)')
for i_num in range(1, number_of_order+1):
    order = input('{0} заказ: '.format(i_num))
    order_list = order.split(' ')
    if order_list[0] not in main_order_dict.keys():
        main_order_dict[order_list[0]] = {order_list[1]: int(order_list[2])}
    elif order_list[0] in main_order_dict.keys():
        if order_list[1] not in main_order_dict[order_list[0]].keys():
            main_order_dict[order_list[0]].update({order_list[1]: int(order_list[2])})
        else:
             main_order_dict[order_list[0]][order_list[1]] += int(order_list[2])
for client in main_order_dict.keys():
    print(client, ': ')
    for orders in main_order_dict[client]:
        print(f'\t\t{orders}: {main_order_dict[client][orders]}')
