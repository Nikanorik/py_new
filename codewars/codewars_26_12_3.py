def max_sequence(arr):
    print(arr)
    count=0
    for b in arr:
        if b<0:
            count+=1
            if count==len(arr):
                return 0
    if arr==[]:
        return 0
    else:
        list = []
        for i in range(len(arr)):
            summa = 0
            for a in range(i,len(arr)):
                summa+=arr[a]
                if summa > arr[a]:
                    list.append(summa)
        return max(list)






max_sequence([-2, -1, -3, -4, -1, -2, -1, -5, -4])