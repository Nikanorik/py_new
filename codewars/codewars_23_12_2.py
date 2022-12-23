def count_smileys(arr):
    print(arr)

    score=0
    for i in arr:
        count=0
        list=[[';',':'],['-','~'],['D',')']]

        for a in i:
            for b in list:
                if a in b:
                    count+=1
                    list.remove(b)
        if count==len(i):
            score+=1
    print(score)


count_smileys([':)', ':(', ':D', ':O', ':;'])