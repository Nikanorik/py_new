import random


def main():
    print('Welcom in game B&j!!!')
    print('Card are dealt!!!')
    suit = ['Bubi','Chervi','Kresta','Pika']
    denomination = ['Valet','Dama','King','Tuz']
    for i in range(2,11):
        denomination.append(str(i))
    hand1=hand_main(denomination)
    count1 = variant(hand1)
    print(f'hand1 = {hand1} {random.choice(suit)} and count= {count1}')
    hand1_new = so_card(count1,denomination)
    print(f'count1= {hand1_new}')
    hand2 = hand_main(denomination)
    count2 = variant(hand2)
    print(f'hand2 = {hand2} {random.choice(suit)} and count= {count2}')
    hand2_new = so_card(count2,denomination)
    print(f'count2= {hand2_new}')




def variant(denomination):
    if denomination == 'Valet' or denomination=='Dama' or denomination == 'King' or denomination== 'Tuz':
        return 10
    else:
        return int(denomination)
def hand_main(denomination):
    hand = random.choice(denomination)
    return hand
def so_card(count,denomination):
    if count<=18:
        new_hand= hand_main(denomination)
        count+=variant(new_hand)
        return count
    else:
        return count





if __name__ == '__main__':
    main()