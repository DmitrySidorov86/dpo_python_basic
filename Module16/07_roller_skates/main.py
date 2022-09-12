rollers = int(input('Количество коньков: '))
rollers_list = []

for i_rollers in range(rollers):
    shoe_size = int(input(f'Размер {i_rollers+1} пары: '))
    rollers_list.append(shoe_size)

rollerman_list = []
rollerman = int(input('Количество людей: '))

for i_rollerman in range(rollerman):
    shoe_size_man = int(input(f'Размер ноги {i_rollerman+1} человека: '))
    rollerman_list.append(shoe_size_man)

rollers_list.sort()
new_rollers_list = rollers_list
rollerman_list.sort(reverse=True)
coincidence = 0

for i_rollerman in range(len(rollerman_list)):
    for i_rollers in range(len(new_rollers_list)):
        if rollerman_list[i_rollerman] <= new_rollers_list[i_rollers]:
            coincidence += 1
            new_rollers_list.remove(new_rollers_list[i_rollers])
            new_rollers_list.append(0)
            break

print(coincidence)