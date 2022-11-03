def is_isogram():
    text = input('Enter text: ')
    a=-len(text)
    for i in range(len(text)):
        num = text[i]

        for two in text:

            if num.lower() == two.lower() or num==two!='':
                a+=1
            else:
                a+=0
    if a > 0:
        print("same chars may not be adjacent")
        return False

    else:
        print(True)
        return True

is_isogram()