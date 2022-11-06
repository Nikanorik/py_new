def to_jaden_case(string):
    string_new=string.split()
    list_new=[]
    for i in range(len(string_new)):
        if "'" not in string_new[i]:
            up_line = string_new[i].title()
            list_new.append(up_line)
        else:
            result=''
            list_two=string_new[i].split("'")
            result+=list_two[0].title()+"'"+list_two[1]
            list_new.append(result)

    return ' '.join(list_new)




to_jaden_case("How can mirrors be real if our eyes aren't real")