def delete_nth(order,max_e):
    list2=[]
    for i in order:
        amount=1
        for a in list2:
            if a==i:
                amount+=1
        if amount<=max_e:
            list2.append(i)



    return list2



delete_nth([20,37,20,21], 1)