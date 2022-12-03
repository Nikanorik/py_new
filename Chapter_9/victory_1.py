import random
def main():
    dict1 = {'russia':'moscow', 'italy':'rim','usa':'nui-york','germany':'berlin'}
    random_country = random.choice(list(dict1))
    question = input(f'Enter country capital {random_country.upper()} : ').lower()
    if question == dict1[random_country]:
        print('Well')
    else:
        print('Looser')

if __name__ == '__main__':
    main()