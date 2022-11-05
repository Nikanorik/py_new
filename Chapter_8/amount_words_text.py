def main():
    file_new = open('text.txt', 'r')
    summa = 0
    list = []
    up_words = 0
    down_words = 0
    fero = 0
    probel = 0
    for i in file_new:
        for num in i:
            if num.isupper():
                up_words += 1
            elif num.islower():
                down_words += 1
            elif num.isdigit():
                fero += 1
            elif num == ' ':
                probel += 1
        string_list = i.split()
        long_string = len(string_list)
        list.append(long_string)
        summa += long_string
    middel = summa / len(list)

    print(f'Mid amount words: {middel}')
    print(f'Amount Up number: {up_words}')
    print(f'Amount down words: {down_words}')
    print(f'Amount number: {fero}')
    print(f'Amount space: {probel} ')
    file_new.close()


if __name__ == '__main__':
    main()
