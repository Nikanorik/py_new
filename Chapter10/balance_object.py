from balance import Balance


def main():
    first = int(input('Enter first balance: '))
    question= input('You want to contribute money?(y/n): ')
    balance_one=Balance(first)
    if question=='y':
        amount=int(input('Enter money for bank check: '))
        balance_one.deposite(amount)

    else:
        question2=input('You want to take off money? (y/n): ')
        if question2=='y':
            pay=int(input('Enter money for take off: '))
            balance_one.withdraw(pay)
        else:
            print('Thank you!!!')
    print(balance_one)

if __name__ == '__main__':
    main()