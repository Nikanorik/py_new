def get_sum(a,b):
    sum=0
    if b>a:
        for i in range(a,b+1):
            sum+=i
    elif b<a:
        for i in range(b,a+1):
            sum+=i
    elif a==b:
        sum=a
    print(sum)





get_sum(-17,-17)