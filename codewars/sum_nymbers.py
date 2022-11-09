def grow(arr):
    product = 1
    for i in arr:
        product *= i
    return product


grow([1,2,3,4,5,6])