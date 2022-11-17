def main():
    phonebook = {'Kris': '919-555-1111', 'Kat': '828-111', 'Djoanna': '704-555-3333', 'Kurt': '919-555-333'}
    # phone = {k:v.split('-') for k,v in phonebook.items()}
    # phone_one={}
    # for i in phone:
    #     num=phone[i]
    #     if int(num[0])>=919:
    #         phone_one[i]='-'.join(num)
    #
    # print(phone_one)
    phone = {k: v for k, v in phonebook.items() if '919' in v}
    print(phone)


if __name__ == '__main__':
    main()
