def voucher_list(number):
    voucher = []
    for _ in range(number):
        voucher.append(0)
    among = int(input('От кого: '))
    whom = int(input('Кому: '))
    how_many = int(input('Сколько: '))
    voucher[among-1] -= how_many
    voucher[whom-1] += how_many
    return voucher


def balance(man):
    total = 0
    for debt in range(len(receipt_list)):
        total += receipt_list[debt][man]
    return total

friends = int(input('Кол-во друзей: '))
receipt = int(input('Кол-во расписок: '))
receipt_list = []
count = 1
while receipt >= count :
    print(f'\n{count}-я расписка')
    receipt_list.append(voucher_list(friends))
    count += 1


print('\nБаланс друзей')
for i_list in range (friends):
    print(f'{i_list+1}: {balance(i_list)}')
