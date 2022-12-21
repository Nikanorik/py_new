def high(x):
    # Code here
    alphavit='abcdefghijklmnopqrstuvwxyz'
    list=x.split()
    list_n=[]

    for i in list:
        sum = 0
        for a in i:
            number=alphavit.index(a)+1
            sum+=number
        list_n.append(sum)

    return list[list_n.index(max(list_n))]



high('man i need a taxi up to ubud')