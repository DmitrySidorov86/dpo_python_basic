import os

way = open(os.path.join('numbers.txt'), 'r')
file_summ = 0

for num in way:
    num.strip()
    file_summ += int(num)

way.close()
write_file = open('answer.txt', 'w')
write_file.write(str(file_summ))
write_file.close()
