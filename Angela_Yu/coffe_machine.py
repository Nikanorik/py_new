

def main():
    MENU = {
        "espresso": {
            "ingredients": {
                "water": 50,
                "milk":0,
                "coffee": 18,
            },
            "cost": 1.5,
        },
        "latte": {
            "ingredients": {
                "water": 200,
                "milk": 150,
                "coffee": 24,
            },
            "cost": 2.5,
        },
        "cappuccino": {
            "ingredients": {
                "water": 250,
                "milk": 100,
                "coffee": 24,
            },
            "cost": 3.0,
        }
    }

    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }

    def report():
        print(f'Water: {resources["water"]}ml')
        print(f'Milk: {resources["milk"]}ml')
        print(f'Coffee: {resources["coffee"]}g')
    def report_menu(choice):
        print(f"Water: {MENU[choice]['ingredients']['water']}ml")
        print(f"Milk: {MENU[choice]['ingredients']['milk']}ml")
        print(f"Coffee: {MENU[choice]['ingredients']['coffee']}g")
        print(f"Money: {MENU[choice]['cost']}$")
    def comparison_of_values(choice):
        resources["water"] = resources["water"] - MENU[choice]['ingredients']['water']
        resources["milk"] = resources["milk"] - MENU[choice]['ingredients']['milk']
        resources["coffee"] = resources["coffee"] - MENU[choice]['ingredients']['coffee']
    def give_money():
        print('Insert money and enter quantity')
        quarters = int(input('Amount quartes: '))*0.25
        dimes = int(input('Amount dimes: '))*0.1
        nickles = int(input('Amount nickels: '))*0.05
        pennies = int(input('Amount pennies: '))*0.01
        money= quarters+dimes+nickles+pennies
        return money




    choice = input('What would you like!(espresso/latte/cappuccino) ').lower()
    while choice not in 'off':
    #What would you like?(expresso/latte/cappuccino)

        if choice == 'report':
            report()
            choice = input('What would you like!(espresso/latte/cappuccino) ').lower()
        elif choice == 'espresso':
            report_menu(choice)
            comparison_of_values(choice)
        elif choice == 'latte':
            report_menu(choice)
            comparison_of_values(choice)
        elif choice == 'cappuccino':
            report_menu(choice)
            comparison_of_values(choice)
        if resources["water"]>0 and resources["milk"]>0 and resources["coffee"]>0:
            result = give_money()- MENU[choice]['cost']
            if result>0:
                print('Thank you! Your drink is ready!')
                report()
                print(f'Remainder Money: ${result:.2f}')
                choice = input('What would you like!(espresso/latte/cappuccino) ').lower()

            else:
                while result < 0:
                    print(f'Not enough money: {abs(result):.2f}')
                    result += give_money()
                print('Thank you! Your drink is ready!')
                report()
                print(f'Remainder Money: ${result:.2f}')
                choice = input('What would you like!(espresso/latte/cappuccino) ').lower()
        elif resources["water"]<0:
            print('Sorry! Little water!!!')
            choice='off'
        elif resources["milk"]<0:
            print('Sorry! Little milk!!!')
            choice = 'off'
        elif resources["coffee"]<0:
            print('Sorry! Little coffee!!!')
            choice = 'off'








#Turn off in coffee_machine ('off')


# Check resourse



# Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01

# Transaction

#Cook coffee

if __name__ == '__main__':
    main()
