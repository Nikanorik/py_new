def find_it(seq):
    for i in seq:
        amount=seq.count(i)
        if amount%2!=0:
            print(i)
            return i





find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5])