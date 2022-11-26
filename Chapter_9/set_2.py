import pickle

def main():
    file = open('test.dat','rb')

    flag = True
    while flag:
        try:
            person = pickle.load(file)
            display(person)
            flag = input('Next?:(y/n) ').lower()
            print()
            if flag == 'y':
                flag=True
        except EOFError:
            flag = False
            print('End!')



    file.close()
def display(person):
    print('Name: ',person['name'])
    print('Age: ', person['age'])
    print('Country: ', person ['country'])
    print()
if __name__ == '__main__':
    main()

