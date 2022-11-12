def reverse_words(text):
    text_line=text.split()

    text_line2=[]
    text_line3=''
    for i1 in text_line:
        text_new = ''
        for i2 in i1[-1::-1]:
            text_new+=i2
        text_line2.append(text_new)
    for i3 in text_line2:
        text_line3+=i3+' '
    # text_line3=' '.join(text_line2)
    print(text_line3)
    return text_line3





reverse_words('sihT si na !elpmaxe')


