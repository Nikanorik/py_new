def main(text):
    list = text.split()
    list_new=''
    for i in list:
        list_new+=i
    apport=list_new[::-1]
    print(apport)
if __name__ == '__main__':
    main('Totty by troty')