import random


def main():
    print('Welcom in game B&j!!!')
    print('Card are dealt!!!')
    suit = ['Bubi','Chervi','Kresta','Pika']
    denomination = ['Valet','Dama','King','Tuz']
    for i in range(2,11):
        denomination.append(str(i))
    summa1=function_card(denomination)
    print(f'Hand user = {summa1} {mast(suit)}')
    summa2 = function_card(denomination)
    print(f'Hand comp = {summa2} {mast(suit)}')
    if summa1>summa2 and summa1<=21:
        print('Winner User!!!')
    elif summa2>summa1 and summa2<=21:
        print('Winner Comp!!!')
    elif summa2==summa1 and summa2<=21:
        print('Draw!!!')
    elif summa2>21 and summa1<=21:
        print('Winner User!!! Comp Bust!!!')
    elif summa1>21 and summa2<=21:
        print('Winner Comp!!! User Bust!!!')
    else:
        print('Double Bust!!!')


def hand(denomination):
    hand_new=random.choice(denomination)
    return hand_new
def mast(suit):
    mast_new=random.choice(suit)
    return mast_new
def count_one(count, summa):
    if count=='Valet' or count=='King' or count=='Dama':
        return 10
    elif count=='Tuz' and summa<=10:
        return 11
    elif count=='Tuz' and summa>10:
        return 1
    else:
        return int(count)
def function_card(denomination):
    summa = 0
    while summa <= 15:
        count = hand(denomination)
        amount = count_one(count, summa)
        summa += amount
    return summa









if __name__ == '__main__':
    main()