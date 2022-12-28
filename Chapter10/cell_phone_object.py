import pickle
from cell_phone import CellPhone


def main():
    file_new=open('ceel_phone.dat','wb')
    phones=make()
    pickle.dump(phones,file_new)
    display(phones)
    file_new.close()



def make():
    list_phone=[]
    for i in range(1,6):
        my_phone=input('Enter manufact phone: ')
        my_model = input('Enter model phone: ')
        my_price = float(input('Enter price phone: '))
        phone=CellPhone(my_phone,my_model,my_price)
        list_phone.append(phone)
    return list_phone
def display(phones):
    for i in phones:
        print(i.get_manufact())
        print(i.get_model())
        print(i.get_price())
        print('_________________________')






if __name__ == '__main__':
    main()


