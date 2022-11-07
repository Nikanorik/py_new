def main():
    text = input('Enter text: ')
    text2=text.lower()
    list = []
    list2 = []
    for i in text2:
        c = 0
        if i not in list and i!=' ':
            for b in text2:
                if i==b:
                    c+=1
            list.append(i)
            list2.append(c)
            print(f'{i}={c}')
    maximum = max(list2)
    for num in range(len(list2)):
        if list2[num] == maximum:
            print(f'Max symbol = "{list[num]}" and amount repetition = {maximum}')


main()
