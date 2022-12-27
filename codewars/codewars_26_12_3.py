def max_sequence(arr):
    print(arr)
    list = []
    summa = 0
    for a in range(len(arr)):
        summa += arr[a]
        if summa>=0:
            list.append(summa)
        else:
            summa=0
    if list == [] or arr == []:
        return 0
    else:
        return max(list)


max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])