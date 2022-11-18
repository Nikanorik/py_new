from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options=menu.get_items()
    question = input(f'What would you like? {options}: ')
    if question=='report':
        coffee_maker.report()
        money_machine.report()
    elif question == 'off':
        is_on = False
    else:
        drink = menu.find_drink(question)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)



