import random
list_simpl = [random.randint(0, 10) for _ in range(10)]
print(f'Оригинальный список:{list_simpl}')
new_list = []
for index in range(0, len(list_simpl), 2):
    new_list.append((list_simpl[index], list_simpl[index+1]))
print(new_list)
new_list_one = [(list_simpl[index], list_simpl[index+1]) for index in range(0, len(list_simpl), 2)]
print(new_list_one)
