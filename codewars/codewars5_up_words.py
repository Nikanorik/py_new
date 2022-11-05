def to_jaden_case(string):
    text_new = string.split()
    text_one=''
    for i in text_new:
        i[0]=i[0].upper()
        text_one+=i


to_jaden_case("How can mirrors be real if our eyes aren't real")