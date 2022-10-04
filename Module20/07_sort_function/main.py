def tpl_sort(old_tuple):
    for element in old_tuple:
        if isinstance(element, float):
            return old_tuple
    new_tuple = tuple(sorted(list(old_tuple)))
    return new_tuple
