import datetime


def chat_write(user, text):
    with open('chatlog.txt', 'a', encoding='utf8') as chat_log:
        message = str(datetime.datetime.now()) + ':' + user + ':' + text + '\n'
        chat_log.write(message)


def chat_print():
    with open('chatlog.txt', 'r', encoding='utf8') as chat_log:
        for line in chat_log:
            line.strip('\n')
            print(line)


create_chatlog = open('chatlog.txt', 'w', encoding='utf8')
create_chatlog.close()
name = input('Введите имя пользователя: ')
while True:
    action = int(input('Что вы хотите сделать:\n1)Посмотреть текущий текст чата (нажмите 1).'
                       '\n2)Отправить сообщение(нажмите 2).\n'))
    if action == 1:
        chat_print()
    elif action == 2:
        client_text = input('Ведите сообщение:')
        chat_write(name, client_text)
        chat_print()
