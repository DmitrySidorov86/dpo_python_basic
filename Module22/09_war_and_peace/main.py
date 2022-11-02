import zipfile
import os

zip_book = os.path.abspath(os.path.join('voyna-i-mir.zip'))
zip_book_open = zipfile.ZipFile(zip_book, 'r')
zip_book_open.extract('voyna-i-mir.txt')
letter_dict = dict()
for symbol in open('voyna-i-mir.txt', 'r', encoding='utf8').read():
    if symbol not in letter_dict.keys() and symbol.lower().isalpha():
        letter_dict[symbol] = 1
    elif symbol in letter_dict.keys():
        letter_dict[symbol] += 1
new_analysis_dict = dict(sorted(letter_dict.items(), key=lambda x: x[1], reverse=True))
for key, values in new_analysis_dict.items():
    print(f'Символ "{key}" встречается {values} раз')

