def xo(s):
    print(s)
    text = s.lower()
    score1 = 0
    score2 = 0
    score3 = 0
    for i in text:
        if i == 'x':
            score1 += 1
        elif i == 'o':
            score2 += 1
        else:
            score3 += 1
    if (score1 == score2) or (score3 > 0 and (score1 == 0 and score2 == 0)):
        print(True)
        return True
    else:
        print(False)
        return False


xo('xo0')
