def main():
    # option 1
    # dict1 = {'CS101':3004,'CS102':4501,'CS103':6755,'CS104':1244,'CS105':1411}
    # dict2 = {'CS101':'Haines','CS102':'Alvardo','CS103':'Rich','CS104':'Berk','CS105':'Li'}
    # dict3 = {'CS101':'8:00','CS102':'10:00','CS103':'11:00','CS104':'12:00','CS105':'13:00'}
    # enter_number = input('Enter number course: ')
    # print(f'number cabinet = {dict1[enter_number]}; teacher = {dict2[enter_number]}; time = {dict3[enter_number]}')
    # option 2
    dict4 = {'CS101': ['3004', 'Haines', '8:00'], 'CS102': ['4501', 'Alvardo', '10:00'],
             'CS103': ['6755', 'Rich', '11:00'], 'CS104': ['1244', 'Berk', '12:00'],
             'CS105': ['1411', 'Li', '13:00']}
    enter_number = input('Enter number course: ')
    print(
        f'number cabinet = {dict4[enter_number][0]}; teacher = {dict4[enter_number][1]}; time = {dict4[enter_number][2]}')


if __name__ == '__main__':
    main()
