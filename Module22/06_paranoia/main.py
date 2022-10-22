def change_one(simbl, count):
    for element in alphabet:
        if simbl == letter:
            return alphabet[(alphabet.index(element) + count) % len(alphabet)]


def print_text(file):
    text = open(file, 'r')
    for string in text:
        print(string, end='')
    text.close()


caesar_count = 1
alphabet = '!"#$%&"()*+,-./:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
file_text = open('text.txt', 'w')
word = input('Введите слово для шифровки: ')

for _ in range(4):  # заполняем файл текстом
    file_text.write(f'{word}\n')

file_text.close()
file_text = open('text.txt', 'r')
file_cipher_text = open('cipher_text.txt', 'w')

for line in file_text:
    for symbol in line:
        if symbol in alphabet:
            letter = change_one(symbol, caesar_count)
            file_cipher_text.write(letter)
    file_cipher_text.write('\n')
    caesar_count += 1

file_text.close()
file_cipher_text.close()
print('Содержимое файла: text.txt')
print_text('text.txt')
print()
print('Содержимое файла: cipher_text.txt')
print_text('cipher_text.txt')
