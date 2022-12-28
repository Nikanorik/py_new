def count_sheep(n):
    return ''.join(f'{i} sheep...' for i in range(1,n+1))
count_sheep(0)