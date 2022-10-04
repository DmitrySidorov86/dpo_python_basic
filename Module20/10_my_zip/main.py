def comparison(text, tuple_one):
    if len(text) <= len(tuple_one):
        return len(list(text))
    else:
        return len(tuple_one)


text_list = 'abcd'
simple_tuple = (10, 20, 30, 40, 50)

zip_why = ((text_list[x], simple_tuple[x]) for x in range(comparison(text_list, simple_tuple)))

print(zip_why)

for tuple_two in zip_why:
    print(tuple_two)
