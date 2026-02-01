from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from coffee_logo import logo
from prettytable import PrettyTable
menu=Menu()
coffee_maker=CoffeeMaker()
money_machine=MoneyMachine()
def start():
    print(logo)
    table=PrettyTable()
    table.add_column("Menu",["Latte","Espresso","Cappuccino"])
    table.add_column("Price",["$2.50","$1.50","$3.00"])
    table.align="l"
    print(table)
def Coffee_Machine():
    coffee=True
    while coffee:
        start()
        order_name=input(f"What would you like? {menu.get_items()}:").lower()
        if order_name=="off":
            print("UNDER MAINTENANCE")
            break
        if order_name=="report":
            coffee_maker.report()
            money_machine.report()
            continue
        pick = menu.find_drink(order_name)
        if pick is None:
            continue
        if coffee_maker.is_resource_sufficient(pick):
            if money_machine.make_payment(pick.cost):
                coffee_maker.make_coffee(pick)

Coffee_Machine()
