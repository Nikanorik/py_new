def longest_consec(strarr, k):


    if len(strarr)==0 or k>len(strarr) or k<=0:
        return ''
    else:
        list = []
        for i in range(len(strarr)):
            list_sr=strarr[i:(i+k)]
            stroke=''
            for b in list_sr:
                stroke+=b
            list.append(stroke)
            list2=[]
        for a in list:
            long=len(a)
            list2.append(long)
        maximum=max(list2)
        return list[list2.index(maximum)]










longest_consec(['ejjjjmmtthh', 'zxxuueeg', 'aanlljrrrxx', 'dqqqaaabbb', 'oocccffuucccjjjkkkjyyyeehh'],2)