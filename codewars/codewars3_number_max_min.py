def high_and_low(numbers):
    list = numbers.split()
    list_new = []
    for i in list:
        list_new.append(int(i))
    maximum = max(list_new)
    minimum = min(list_new)
    print(f'{maximum} {minimum}')
    return f'{maximum} {minimum}'
high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4")