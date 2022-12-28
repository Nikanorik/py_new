from cell_phone import CellPhone


def main():
    my_phone=input('Enter manufact phone: ')
    my_model = input('Enter model phone: ')
    my_price = float(input('Enter price phone: '))
    phone=CellPhone(my_phone,my_model,my_price)
    print(f'Your phone: {phone.get_manufact()}, model: {phone.get_model()}, price old: {phone.get_price()}')
    new_price=float(input('Enter new price your phone: '))
    phone.set_price(new_price)
    print(f'Your phone: {phone.get_manufact()}, model: {phone.get_model()}, price new: {phone.get_price()}')



if __name__ == '__main__':
    main()


