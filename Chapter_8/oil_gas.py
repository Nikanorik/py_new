def main():
    file = open('GasPrices.txt', 'r')
    list = []
    list_new = []
    list_mid = []
    list_month_mid = []
    for i in file:
        i = i.rstrip('\n')
        a = i.split(':')
        a[0] = a[0].split('-')
        list.append(a)
    for c in range(1993, 2014):
        sum = 0
        for b in list:
            if int(b[0][2]) == c:
                sum += float(b[1])
        list_new.append(f'{sum:.2f}')
    year = 1992
    for d in list_new:
        year += 1
        mid_number = float(d) / 12
        middel = str(year) + ':' + f'{mid_number:.2f}'
        list_mid.append(middel)
    first = list[0][0][0]
    score = 0
    list_month = []
    for h in list:
        year_first = int(h[0][2])
        if int(h[0][0]) == int(first):
            score += float(h[1])

        else:
            if int(first) == 12:
                year_first = year_first - 1
            list_month.append(year_first)
            list_month.append(first)
            list_month.append(f'{score:.2f}')
            list_month_mid.append(list_month)
            list_month = []
            score = float(h[1])
            first = h[0][0]

    print(list_month_mid)

    print(f'Middel price year: {list_mid}')

    list_main = []
    for max_year in range(1993, 2014):
        list_max_min = []
        list_from = []
        for year_now in list_month_mid:

            if year_now[0] == max_year:
                list_from.append(float(year_now[2]))
        list_max_min.append(f'Year: {max_year}')
        maximum_first = max(list_from)
        list_max_min.append(f'Maximum: {maximum_first}')
        minimum_first = min(list_from)
        list_max_min.append(f'Minimum: {minimum_first}')
        list_main.append(list_max_min)
    print(list_main)


if __name__ == '__main__':
    main()
