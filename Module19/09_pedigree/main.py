people_num = int(input('Введите количество человек: '))
people_dict = dict()
all_people = dict()

for count in range(people_num - 1):
	person, parents = input(f'{count + 1} пара: ').split()
	people_dict[person] = parents
	all_people[person] = 0
	all_people[parents] = 0

for i in people_dict:
	name = i
	while name in people_dict.keys():
		name = people_dict[name]
		all_people[i] += 1

print('\nВысота» каждого члена семьи:')
for i_name in all_people:
	print(i_name, all_people[i_name])