def DNA_strand(dna):
    str_new=''
    for i in dna:
        if i=='A':
            i='T'
            str_new+=i
        elif i=='T':
            i='A'
            str_new += i
        elif i=='C':
            i='G'
            str_new += i
        elif i=='G':
            i='C'
            str_new += i
    return str_new







DNA_strand("ATTGC")