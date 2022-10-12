def fac(data, dict_fact={}):
    if data not in dict_fact.keys():
        if data == 1:
            return 1
        number = fac(data-1)*data
        dict_fact[data] = number
    else:
        number = dict_fact[data-1]*data
    return number


def calculating_math_func(data, first_degree=3, second_degree=10):
    if data == 0:
        print('Деление на ноль приведет к распаду Вселенной. Ты этого хочешь ?')
        return 0
    result = fac(data)
    result /= data ** first_degree
    result = result ** second_degree
    return result


while True:
    numero = int(input('Введите число:'))
    number_one = calculating_math_func(numero)
    if number_one != 0:
        print(number_one)
