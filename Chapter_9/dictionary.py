import random
def main():
    choice_computer = random.randint(1,4)
    choice_user = int(input('Enter amount card you want: '))
    comp = 0
    humen = 0

    for i in range(choice_computer):
        deck_comp = random.choice(list(create_deck()))
        comp+=create_deck()[deck_comp]
    for a in range(choice_user):
        deck_user = random.choice(list(create_deck()))
        humen+=create_deck()[deck_user]
    if comp==humen and comp<=21:
        print(f'Score: {comp} Draw!!!')
    elif comp>humen and comp<=21:
        print(f' Score comp: {comp} and score user: {humen}. Win comp!')
    elif humen>comp and humen<=21:
        print(f'Score comp: {comp} and score user: {humen}. Win user!')
    elif humen>21 and comp>21:
        print(f'Score comp: {comp} and score user: {humen}. Second too much!!!')
    elif humen>21:
        print(f'Score comp: {comp} and score user: {humen}. User have too much!!! Win comp!')
    elif comp>21:
        print(f'Score comp: {comp} and score user: {humen}. Comp have too much!!! Win user!')












def create_deck():
    # Создать словарь, в котором каждая карта и ее значение
    # хранится в виде пар ключ/значение.
    deck = {'Туз пик': 1, '2 пик': 2, '3 пик': 3,
            '4 пик': 4, '5 пик': 5, '6 пик': 6,
            '7 пик': 7, '8 пик': 8, '9 пик': 9,
            '10 пик': 10, 'Валет пик': 10,
            'Дама пик': 10, 'Король пик': 10,

            'Туз червей': 1, '2 червей': 2, '3 червей': 3,
            '4 червей': 4, '5 червей': 5, '6 червей': 6,
            '7 червей': 7, '8 червей': 8, '9 червей': 9,
            '10 червей': 10, 'Валет червей': 10,
            'Дама червей': 10, 'Король червей': 10,

            'Туз треф': 1, '2 треф': 2, '3 треф': 3,
            '4 треф': 4, '5 треф': 5, '6 треф': 6,
            '7 треф': 7, '8 треф': 8, '9 треф': 9,
            '10 треф': 10, 'Валет треф': 10,
            'Дама треф': 10, 'Король треф': 10,

            'Туз бубей': 1, '2 бубей': 2, '3 бубей': 3,
            '4 бубей': 4, '5 бубей': 5, '6 бубей': 6,
            '7 бубей': 7, '8 бубей': 8, '9 бубей': 9,
            '10 бубей': 10, 'Валет бубей': 10,
            'Дама бубей': 10, 'Король бубей': 10}

    # Вернуть колоду.
    return deck


if __name__ == '__main__':
    main()