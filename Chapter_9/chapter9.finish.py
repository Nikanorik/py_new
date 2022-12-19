def main():
    file=open('Kennedy.txt','r')
    file_new = open('New_Kennedy.txt', 'w')
    list=[]
    for i in file:
        new_str=i.split()
        list.append(new_str)
    list_new={}
    for a in list:
        for b in a:
            list_two=[]

            for a in list:
                if b in a:
                    list_two.append(list.index(a)+1)
            list_new[b]=list_two
    for key,value in list_new.items():
        str_first = ' '
        for x in value:
            str_first+=str(x)+' '
        str_new=f'{key}:{str_first}\n'
        file_new.write(str_new)


    print(list_new)





    file.close()
    file_new.close()








if __name__ == '__main__':
    main()