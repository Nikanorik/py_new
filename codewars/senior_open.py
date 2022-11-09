def open_or_senior(data):
    list = []
    for i in data:
        if i[0] >= 55 and i[1] > 7:
            list.append('Senior')

        else:
            list.append('Open')

    print(list)
    return list


open_or_senior([[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]])
