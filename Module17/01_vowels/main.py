text = input('Введите текст: ')
vowels_sample_list = 'ЙйУуЕеЫыАаОоЭэЁёИиЮюEeYyUuOoAa'
vowels_list = [x for x in text if x in vowels_sample_list ]

print(f'Список гласных: {vowels_list}')
print(f'Длинна списка : {len(vowels_list)}')