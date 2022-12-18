def is_valid_walk(walk):
    list_one = ['n','s','w','e']
    list_two=[]
    for i in list_one:
        amount=walk.count(i)
        list_two.append(amount)
    if len(walk)==10 and list_two[0]==list_two[1] and list_two[2]==list_two[3]:
        return True
    else:
        return False





is_valid_walk(['n','s','n','s','n','s','n','s','n','s'])