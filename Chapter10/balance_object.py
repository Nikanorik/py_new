from balance import Balance


def main():
    first = int(input('Enter first balance: '))
    question= input('You want to contribute money?(y/n): ')
    balance_one=Balance(first)
    if question=='y':
        amount=int(input('Enter money for bank check: '))
        balance_one.deposite(amount)
        print(f'Your balance: {balance_one.get_balance()}')

    else:
        question2=input('You want to take off money? (y/n): ')
        if question2=='y':
            pay=int(input('Enter money for take off: '))
            balance_one.withdraw(pay)
            print(f'Your balance: {balance_one.get_balance()}')
        else:
            print('Thank you!!!')

if __name__ == '__main__':
    main()