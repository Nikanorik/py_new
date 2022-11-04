def nb_year(p0, percent, aug, p):
    people = p0
    i=0
    while people < p:
        people = int(people+people*(percent/100)+aug)
        i+=1
    print(f'It will need {i} years')
    return i
nb_year(1000, 2.0, 50, 1214)

