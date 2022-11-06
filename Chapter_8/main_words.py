def main():
    text = input('Enter text: ')
    podbor(text)


def podbor(string):
    new_text = string.split()
    string_line = []
    for i in range(len(new_text)):
        if i == 0:
            the_first = new_text[0].title()
            string_line.append(the_first)
        elif i == -1:
            string_line.append(new_text[i])
        elif i != -1:
            if new_text[i][-1] == '.' or new_text[i][-1] == '!' or new_text[i][-1] == '?':
                string_line.append(new_text[i])
            elif i  <= (len(new_text) - 1) and (
                    new_text[i - 1][-1] == '.' or new_text[i - 1][-1] == '!' or new_text[i - 1][
                -1] == '?') and i - 1 >= 0:
                the_third = new_text[i].title()
                string_line.append(the_third)
            else:
                string_line.append(new_text[i])
    new_string_line = ' '.join(string_line)
    print(new_string_line)


if __name__ == '__main__':
    main()
