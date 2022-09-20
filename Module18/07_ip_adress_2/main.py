
while True:
    ip_adress = input('Введите IP:')
    error = 0
    ip_list = ip_adress.split('.')
    if len(ip_list) < 4 :
        print('Адрес — это четыре числа, разделённые точками.')
        error += 1
    else:
        for i in ip_list:
            if not i.isdecimal():
                print(f'{i} - это не целое число.')
                error += 1
            elif 0 < int(i) > 255:
                print(f'{i} превышает 255.')
                error += 1
    if error == 0:
        print('IP-адрес корректен.')
        break