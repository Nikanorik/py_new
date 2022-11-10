def main():
    file = open('pbnumbers.txt', 'r')
    list={}
    for i in file:
        i=i.rstrip('\n')
        new = i.split()
        for num in new:
            if num!=' ':
                if num in list:
                    list[num]+=1
                else:
                    list[num]=1
    list_max=max(list.values())
    print(list)


if __name__ == '__main__':
    main()

