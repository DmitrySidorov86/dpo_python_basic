first = input('Первая строка:')
second = input('Вторая строка:')
first_list = list(first)
even = False
for shift in range(1,len(first_list)):
    first_list += first_list.pop(0)
    if ''.join(first_list) == second:
        print(f'Первая строка получается из второй со сдвигом {shift}.')
        even = True
        break
if even == False:
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')



