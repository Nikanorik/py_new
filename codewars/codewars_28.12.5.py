def number(lines):
    #your code here
    print(lines)
    list=[]
    if lines!=[]:
        for i in range(len(lines)):
            list.append(f'{i+1}: {lines[i]}')
    else:
        return []
    return list



number(["a", "b", "c"])