def square_digits(num):
    sum=''
    for i in str(num):
        numer=int(i)**2
        sum+=str(numer)
    return int(sum)


square_digits(9119)