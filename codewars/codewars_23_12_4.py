def duplicate_encode(word):
    new = word.lower()
    str=''
    for i in new:
        if word.count(i)>1:
            str+=')'
        else:
            str+='('
    # return (str for i in word if word.count(i)>i str+=')' else str+='(' )
    return str



duplicate_encode("Success")