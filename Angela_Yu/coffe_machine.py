

def main():
    MENU = {
        "espresso": {
            "ingredients": {
                "water": 50,
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




    choice = input('What would you like!(espresso/latte/capuccino) ').lower()
    while choice not in 'off':
    #What would you like?(expresso/latte/capuccino)

        if choice == 'report':
            report()
        elif choice == 'espresso':
            comparison_of_values(choice)
        elif choice == 'latte':
            comparison_of_values(choice)
        elif choice == 'capuccino':
            comparison_of_values(choice)
        if resources["water"]>0 and resources["milk"]>0 and resources["coffee"]>0:
            result = give_money()- MENU[choice]['cost']
            if result>0:
                print('Thank you! Your drink is ready!')
                choice = input('What would you like!(espresso/latte/capuccino) ').lower()
                report()
                print(f'Remainder Money: ${result:.2f}')
            else:
                result = give_money() - MENU[choice]['cost']





#Turn off in coffee_machine ('off')


# Check resourse



# Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01

# Transaction

#Cook coffee

if __name__ == '__main__':
    main()
