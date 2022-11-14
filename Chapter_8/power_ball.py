def main():
    file = open('pbnumbers.txt', 'r')
    list_new = []
    list_second = []
    list_third = []
    for i in file:
        i = i.rstrip('\n')
        list = i.split()
        for a in list:
            list_new.append(a)
            a = int(a)
            list_third.append(a)
    for b in list_new:
        number = list_new.count(b)
        list_second.append(number)
    list1 = []
    list2 = []
    for c in range(10):
        maximum = max(list_second)
        minimum = min(list_second)
        index_minimum = list_second.index(minimum)
        index_maximum = list_second.index(maximum)
        print(f'Max number {c + 1} = {list_new[index_maximum]}')
        list1.append(list_new[index_maximum])
        print(f'Min number {c + 1} = {list_new[index_minimum]}')
        list2.append(list_new[index_minimum])
        list_new.remove(list_new[index_maximum])
        list_new.remove(list_new[index_minimum])
    print(f'Maximum number = {list1}')
    print(f'Minimum number = {list2}')

    list_fourth = []
    for h in range(1, 70):
        plus = list_third.count(h)
        plus2 = str(h) + ':' + str(plus)
        list_fourth.append(plus2)
        print(f'Frequency number {h} = {plus}')
    print(list_fourth)

    file.close()


if __name__ == '__main__':
    main()
