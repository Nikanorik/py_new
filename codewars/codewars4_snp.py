def main(name):
    string_name = ''
    for i in name:
        if i.isupper():
            string_name+=i+'.'
    print(string_name)
if __name__ == '__main__':
    main('Gubanov Sasha Mihailovich')
