zen_open = open('zen.txt', 'r')
zen_list = list()
for string in zen_open:
    zen_list.append(string.replace('\n', ''))
zen_open.close()
for index in range(1, len(zen_list)+1):
    print(zen_list[-index])
