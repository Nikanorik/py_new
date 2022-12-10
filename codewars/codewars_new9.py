def unique_in_order(iterable):
    list_new = []

    for i in range(len(iterable)):

        if (i-1)>=0:
            if iterable[i]!=iterable[i-1]:
                list_new.append(iterable[i])
        elif (i-1)<0:
            list_new.append(iterable[i])


    return list_new


unique_in_order([1,2,2,3,3])