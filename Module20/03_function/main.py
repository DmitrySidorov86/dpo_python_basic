def slicer(tuple_old, cut):
    if cut in tuple_old:
        if list(tuple_old).count(cut) == 1:
            for index, value in enumerate(tuple_old):
                if value == cut:
                    new_tuple = tuple(tuple_old[index:])
        elif list(tuple_old).count(cut) > 1:
            start = 0
            end = 0
            for index, value in enumerate(tuple_old):
                if value == cut:
                    if start == 0:
                        start = index
                    elif start != 0 and end == 0:
                        end = index
            new_tuple = tuple(tuple_old[start:end+1])
    else:
        new_tuple = tuple()
    return new_tuple
