import random

stick = int(input('Количество палок: '))
check_list =[x for x in range(1,stick+1)]
check_list_One = check_list[:]
throw = int(input('Количество бросков: '))

for i in range(throw):
    left_i = random.randint(0,len(check_list_One)-1)
    right_i = random.randint(left_i, len(check_list_One)-1)
    print(f'Бросок {i+1}. Сбиты палки с номера {check_list_One[left_i]} по номер {check_list_One[right_i]}')
    del check_list_One[left_i:right_i+1]




stand_list = ['l' if check_list[i_list] in check_list_One else '.' for i_list in range(len(check_list)) ]
print("".join(stand_list))

