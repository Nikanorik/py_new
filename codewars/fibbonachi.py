def tribonacci(signature, n):
    alfa=signature
    if n>=3:
        for i in range(n-3):
            b=alfa[-1]+alfa[-2]+alfa[-3]
            alfa.append(b)
    elif n==0:
        return []
    elif n<3:
        return alfa[:n]

    return alfa





tribonacci([300, 200, 100], 0)