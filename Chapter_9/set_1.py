import pickle
def main():
    file = open('test.dat','wb')
    flag = 'y'
    while flag=='y':
        repeat_print(file)
        flag = input('Do you want to next?(y/n) ').lower()
    file.close()

def repeat_print(file):
    person={}
    person['name']=input('Enter name: ')
    person['age']= input('Enter age: ')
    person['country'] = input('Enter country: ')
    pickle.dump(person,file)





if __name__ == '__main__':
    main()