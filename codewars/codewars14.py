def descending_order(num):
    new=str(num)
    list=[]
    for i in new:
        list.append(i)
    new_one = sorted(list,reverse=True)
    new_two = ''.join(new_one)
    return int(new_two)






descending_order(42145)