def filter_list(l):
    'return a new list with the strings filtered out'
    list=[]
    for i in l:
        if type(i)==int:
          list.append(i)
    print(list)





filter_list([1,'2',5,6,'Ab'])