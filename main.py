from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

drink_menu = Menu()


def menu_selection():
    drink_menu.get_items()
    drink_menu.print_menu_banner()


def is_drink_available(drink_name):
    #  TODO - add else
    drink = drink_menu.find_drink(drink_name)
    if drink is not None:
        return drink


def process_order():
    selected_drink = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    ordered_drink = selected_drink.menu_selection()  # returns a drink

    while True:
        if ordered_drink == "latte":
            latte = is_drink_available(ordered_drink)
            if latte:
                print(f"{ordered_drink}\t\t ${latte.cost}")
                if coffee_maker.is_resource_sufficient(latte):
                    f"{money_machine.report()}\n"
                if money_machine.make_payment(latte.cost):
                    coffee_maker.make_coffee(latte)
                    f"{money_machine.report()}\n"
                    break
        elif ordered_drink == "espresso":
            expresso = is_drink_available(ordered_drink)
            if expresso:
                print(f"{ordered_drink}\t\t ${expresso.cost}")
                if coffee_maker.is_resource_sufficient(expresso):
                    f"{money_machine.report()}\n"
                if money_machine.make_payment(expresso.cost):
                    coffee_maker.make_coffee(expresso)
                    f"{money_machine.report()}\n"
                    break
        elif ordered_drink == "cappuccino":
            cappuccino = is_drink_available(ordered_drink)
            if cappuccino:
                print(f"{ordered_drink}\t\t ${cappuccino.cost}")
                if coffee_maker.is_resource_sufficient(cappuccino):
                    f"{money_machine.report()}\n"
                if money_machine.make_payment(cappuccino.cost):
                    coffee_maker.make_coffee(cappuccino)
                    f"{money_machine.report()}\n"
                    break
        else:
            ...


if __name__ == '__main__':
    menu_selection()
    process_order()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
