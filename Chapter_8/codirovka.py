def main():
    text = input('Enter text for code: ')
    basa_data = {'a': '__1__', 'b': '__2__', 'c': '__3__', 'd': '__4__', 'e': '__5__', 'f': '__6__', 'g': '234',
                 'h': '45',
                 'i': '36', 'j': '254', 'k': '567', 'l': '534', 'm': '6960', 'n': '5450', 'o': '1010', 'p': '4059',
                 'q': '7966',
                 'r': '0_0', 's': '__!!__', 't': '5050', 'u': '53453', 'v': '6060', 'w': '4590469', 'x': '686',
                 'y': '7879',
                 'z': '5959'}
    str_text = ''
    for i in text:
        i = i.lower()
        if i != ' ':
            i = basa_data[i]
            str_text += i
        else:
            i = '!'
            str_text += i
    print(str_text)


if __name__ == '__main__':
    main()
