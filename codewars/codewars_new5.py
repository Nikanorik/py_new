def duplicate_count(text):
    call=0
    text1=text.lower()
    str_new=''
    for i in text1:
        amount=text1.count(i)
        if amount>1 and i not in str_new:
            call+=1
            str_new += i
    print(call)
    return call




duplicate_count("abcdeaB")
