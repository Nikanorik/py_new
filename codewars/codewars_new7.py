def series_sum(n):
    str_new = 0
    if n==1:
        str_new=1
    elif n==2:
        str_new=1+1/4
    elif n>2:
        str_new =1+1/4
        for i in range(3,n+1):
            str_new+=1/(4+(3*i-6))
    return f'{str_new:.2f}'



series_sum(5)