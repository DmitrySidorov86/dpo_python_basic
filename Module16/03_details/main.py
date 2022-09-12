shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

counter = 0
price = 0
name = input('Название детали: ')

for position in shop:
        if position[0] == name:
                counter += 1
                price += position[1]

print(f'Кол-во деталей:{counter}')
print(f'Общая стоимость: {price}')
