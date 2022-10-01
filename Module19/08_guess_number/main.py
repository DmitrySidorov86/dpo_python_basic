max_number = int(input('Введите максимальное число: '))
answer_set = {x for x in range(1, max_number + 1)}
while True:
    question = input('\nНужное число есть среди вот этих чисел:')
    if question == 'Помогите!':
        print('Артём мог загадать следующие числа: ', end=' ')
        for x in sorted(answer_set):
            print(x, end=' ')
        break
    else:
        question_set = {int(x) for x in question.split(' ')}
        answer = input('Ответ Артёма: ')
        if answer.lower() == 'да' or answer.lower() == 'lf':
            answer_set = set(question_set)
        elif answer.lower() == 'нет'or answer.lower() == 'ytn':
            answer_set -= question_set