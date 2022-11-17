find = 1
add = 2
change = 3
delete = 4
quit_n = 5


def main():
    happy = {}
    choice = 0
    print('Wellcom my friend in program Birthday!!!')
    while choice != quit_n:
        choice = get_menu(choice)

        if choice == find:
            find_name(happy)
        elif choice == add:
            add_name(happy)
        elif choice == change:
            change_name(happy)
        elif choice == delete:
            del_name(happy)
        elif choice == quit_n:
            choice = quit_n
    print('Vocabulary close!!! Thank you!!!')


def get_menu(choice):
    if choice == 0:
        print(f'1. Find birthday\n2. Add name and birthday\n3. Change birthday\n4. Delete name and birthday\n5. Exit ')
    choice = int(input('Enter number your variant: '))
    if 0 < choice < 6:
        return choice
    else:
        print('You enter error number!!! Enter from 1 to 5!!!')


def find_name(happy):
    name = input('Enter name for find: ')
    print(happy.get(name, 'Sorry, name is not find'))


def add_name(happy):
    name = input('Enter name: ')
    bday = input('Enter birthday: ')
    if name not in happy:
        happy[name] = bday
    else:
        print('The name is in the dictionary ')


def change_name(happy):
    name = input('Enter a name to replace: ')
    bday = input('Enter new birthday: ')
    if name in happy:
        happy[name] = bday
    else:
        print('The name is not in the dictionary ')


def del_name(happy):
    name = input('Enter name for delete: ')
    if name in happy:
        del happy[name]
    else:
        print('The name is not in the dictionary ')


if __name__ == '__main__':
    main()
