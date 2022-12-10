def main():
    file1=open('text1.txt','r')
    file2=open('text2.txt','r')
    myset1=set()
    myset2=set()
    for i in file1:
        i=i.rstrip('\n')
        myset1.add(i)
    for a in file2:
        a=a.rstrip('\n')
        myset2.add(a)
    inter_one=myset1.intersection(myset2)
    differ_one=myset1.difference(myset2)
    differ_two=myset2.difference(myset1)
    symmetric_difference_one = myset1.symmetric_difference(myset2)
    print(list(myset1))
    print(list(myset2))
    print(f'Intersection: {list(inter_one)}')
    print(f'difference myset1: {list(differ_one)}')
    print(f'difference myset2: {list(differ_two)}')
    print(f'symmetric_difference: {list(symmetric_difference_one)}')

    file1.close()
    file2.close()







if __name__=='__main__':
    main()