def main():
    text=input('Enter Text: ')
    string_new =''
    string_new+=text[0].upper()
    for i in text[1:]:
        if i.islower():
            string_new+=i
        elif i.isupper():
            result = i.lower()
            string_new+=' '+result
    print(string_new)



if __name__ == '__main__':
    main()