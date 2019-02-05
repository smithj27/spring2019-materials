def divby2(x):
    list1 = []
    for item in x:
        if item%2 == 0:
            list1.append(item)
        else:
            continue
    return list1
