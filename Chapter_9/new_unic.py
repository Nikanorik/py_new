def main():
    file = open('code_new.txt','r')
    myset=set()
    for i in file:
        new = i.split()
        for b in new:
            myset.add(b)
    print(myset)



if __name__ == '__main__':
    main()