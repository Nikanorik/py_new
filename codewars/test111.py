def test(x):
    for i in x:
        if x.count(i)>1:
            x.pop(i)
    print(x)

test([0,0,0,1,1,2,2,3,4])