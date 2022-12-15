def digitize(n):
    list_int=[]
    for i in str(n):
        i=int(i)
        list_int.append(i)
    print(list_int[-1::-1])




digitize(23582357)