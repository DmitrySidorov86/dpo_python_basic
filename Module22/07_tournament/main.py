first_file = open('first_tour.txt', 'r')
first_list = []
limit = 0
check = True
gamers_dict = dict()
for line in first_file:
    if check:
        limit = int(line)
        check = False
    else:
        line_list = line.split(' ')
        score = int(line_list[2].replace('\n', ''))
        if score > limit:
            name = str(line_list[1][:1] + '.' + ' ' + line_list[0])
            gamers_dict[name] = score
first_file.close()
gamers_dict = dict(sorted(gamers_dict.items(), key=lambda x: x[1], reverse=True))
second_open = open('second_tour.txt', 'w')
second_open.write(str(len(gamers_dict)))
second_open.write('\n')
count = 1
for key, values in gamers_dict.items():
    text = str(count) + ') ' + key + ' ' + str(values) + '\n'
    second_open.write(text)
    count += 1
