def abbrev_name(name):
    # str_new=name.split(' ')
    # new = []
    # for i in str_new:
    #     new.append(i[0].upper())
    # return '.'.join(new)
    return '.'.join(i[0] for i in name.split()).upper()






abbrev_name("patrick feenan")