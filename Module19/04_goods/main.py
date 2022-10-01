goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for i in store:
    price_all = 0
    quantity_all = 0
    for y in store[i]:
        price_all += y['quantity']*y['price']
        quantity_all += y['quantity']
    print('{0} - {1} штук, стоимостью {2} рубля.'.format(
        list(goods.keys())[list(goods.values()).index(i)],
        quantity_all,
        price_all
    ))

