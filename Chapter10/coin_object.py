from coin import Coin

def main():
    my_cort=Coin()
    print(f'Your side of the coin: {my_cort.get_sideup()}')
    choice= input('Next? (y/n): ')
    while choice=='y':
        my_cort.toss()
        tossing_comp=my_cort.get_sideup()
        my_cort.toss()
        tossing_us=my_cort.get_sideup()
        print(f'Your tossing: {tossing_us} and Computer tossing: {tossing_comp}')
        if tossing_us==tossing_comp:
            print('Draw')
        elif tossing_us=='Eagle':
            print('Winner user!!!')
        else:
            print('Winner Comp!!!')
        choice= input('Next? (y/n): ')
    print('Thank you!!!')


if __name__ == '__main__':
    main()