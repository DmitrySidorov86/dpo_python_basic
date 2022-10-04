def is_prime(variable):
    check = True
    if variable <= 1:
        check = False
    else:
        for i in range(2, round(variable/2) + 1):
            if variable % i == 0:
                check = False
    return check


def crypto(x):
    list_answer = [simbl for index, simbl in enumerate(x) if is_prime(index)]
    return list_answer
