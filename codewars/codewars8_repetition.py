def longest(a1, a2):
    str_new=[]
    for num1 in a1:
        if num1 not in str_new:
            str_new.append(num1)
    for num2 in a2:
        if num2 not in str_new:
            str_new.append(num2)
    str_first = sorted(str_new)
    str_fourth = ''.join(str_first)
    print(str_fourth)
    return str_fourth

longest("loopingisfunbutdangerous", "lessdangerousthancoding")