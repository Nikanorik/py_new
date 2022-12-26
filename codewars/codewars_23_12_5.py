def find_nb(m):
    print(m)
    summer = 1
    count = 1
    cun = 1
    while summer < m:
        cun += 1
        summer += (cun) ** 3
        count += 1
    if summer == m:
        return count
    else:
        return -1


find_nb(4183059834009)