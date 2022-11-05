def main(phone_number):
    number_new = ''
    for i in phone_number:
        i = str(i)
        if i == '-':
            i = '-'
        elif i == 'A' or i == 'B' or i == 'C':
            i = '2'
        elif i == 'D' or i == 'F' or i == 'E':
            i = '3'
        elif i == 'G' or i == 'H' or i == 'I':
            i = '4'
        elif i == 'J' or i == 'K' or i == 'L':
            i = '5'
        elif i == 'M' or i == 'N' or i == 'O':
            i = '6'
        elif i == 'P' or i == 'Q' or i == 'S' or i == 'R':
            i = '7'
        elif i == 'T' or i == 'U' or i == 'V':
            i = '8'
        elif i == 'W' or i == 'X' or i == 'Y' or i == 'Z':
            i = '9'
        number_new += i
    print(number_new)


if __name__ == '__main__':
    main('555-GT-PHONE')
