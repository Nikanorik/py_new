def get_count(sentence):
    volbrs = ['a', 'e', 'i','o', 'u']
    b = 0
    for i in sentence:
        if i in volbrs:
            b += 1
    print(b)
    return b


get_count('aeiou')