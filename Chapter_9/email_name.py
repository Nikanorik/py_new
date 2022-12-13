def main():
    email_dict = {}
    flag=True
    while flag:
        menu()
        question = int(input('Enter number menu: '))
        if question==1:
            email= input('Enter email: ')
            name = input('Enter name user email: ')
            email_dict[email]=name
        elif question == 2:
            email_one = input('Enter email: ')
            email_new = input('Enter new email: ')
            email_dict[email_new]=email_dict.pop(email_one)
        elif question ==3:
            name_one = input('Enter old name: ')
            name_new = input('Enter new name: ')
            for i in email_dict:
                if email_dict[i]==name_one:
                    email_dict[i]=name_new
        elif question==4:
            del_email = input('Enter email for delete: ')
            del email_dict[del_email]
        elif question == 5:
            find_email = input('Enter email: ')
            print(f'{email_dict[find_email]}')
        elif question==10:
            print(email_dict)
        elif question == 6:
            flag=False
    print(email_dict)
    print('Thank you! ')



def menu():
    print('Enter number menu: ')
    print('1. Add email')
    print('2. Add changes email')
    print('3. Add changes name')
    print('4. Delete email ')
    print('5.Find email user ')
    print('6. Exit')
    print('10. Our database: ')







if __name__ == '__main__':
    main()