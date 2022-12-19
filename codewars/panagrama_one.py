def is_pangram(s):
    list_alfavit = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y',
                    'z']
    count=0
    for i in list_alfavit:
        if i in s.lower():
            count+=1
    if count == 26:
        return True
    else:
        return False






is_pangram("The quick, brown fox jumps over the lazy dog!")
