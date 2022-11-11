import random

from art_inst import logo, vs
from game_data import data


def main():
    print(logo)
    account_a = random_main()
    print(f'Compare A: {random_choice(account_a)}')
    print(vs)
    account_b = random_main()
    print(f'Compare B: {random_choice(account_b)}')
    choice = input('Who has more followers? "A" or "B": ').lower()
    flag = True
    score = 0
    while flag:
        if (choice == 'a' and account_a['follower_count'] > account_b['follower_count']) or (
                choice == 'b' and account_a['follower_count'] < account_b['follower_count']):
            score += 1
            print(logo)
            account_a = account_b
            print(f'Compare A: {random_choice(account_a)}')
            print(vs)
            account_b = random_main()
            print(f'Compare B: {random_choice(account_b)}')
            choice = input('Who has more followers? "A" or "B": ').lower()
        else:
            flag = False
    print(f'Sorry! Game finish! You have score={score}')


def random_main():
    account = random.choice(data)
    return account


def random_choice(account):
    name = account['name']
    description = account['description']
    country = account['country']
    return f'{name}, a {description}, from {country}.'


if __name__ == '__main__':
    main()
