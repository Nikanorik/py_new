def main():
    file=open('WorldSeriesWinners.txt','r')
    amount_list=[]
    amount_winner={}
    year_winner={}
    for i in file:
        i=i.rstrip('\n')
        amount_list.append(i)
    for a in amount_list:
        amount=0
        for b in amount_list:
            if a==b:
                amount+=1
        amount_list.remove(a)
        amount_winner[a]=amount
        file.close()
    file_new=open('WorldSeriesWinners.txt','r')
    year_new=1902
    for f in file_new:
        f=f.rstrip('\n')
        year_new+=1
        year_winner[year_new]=f
    file_new.close()
    print(year_winner)
    print(amount_winner)
    enter = int(input('Enter year for present: '))
    if enter!= 1904 and enter!=1994:
        winner_command=year_winner[enter]
        print(winner_command)
        print(f'Winner in {enter} = {winner_command} and count winner {winner_command} = {amount_winner[winner_command]}')
    else:
        print('World series Not played!')










if __name__ == '__main__':
    main()