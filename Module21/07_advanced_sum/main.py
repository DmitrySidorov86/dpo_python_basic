def summ(*args):
    all_summ = 0
    for element in args:
        if isinstance(element, list):
            for union in element:
                all_summ += summ(union)
        else:
            all_summ += element
    return all_summ
