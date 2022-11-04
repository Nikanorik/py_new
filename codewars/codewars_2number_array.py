def binary_array_to_number(arr):
    num=0
    arr.reverse()
    for i in range(len(arr)):
        if arr[i]==1:
            num+=2**i
    return num
binary_array_to_number([0,0,1,0])