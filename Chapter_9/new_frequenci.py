def main():
    file = open('code_new.txt','r')
    myset=set()
    dict_new={}
    for i in file:
        new = i.split()
        for b in new:
            amount=new.count(b)
            dict_new[b]=amount
            myset.add(b)
    print(myset)
    print(dict_new)



if __name__ == '__main__':
    main()