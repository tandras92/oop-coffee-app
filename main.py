from menu import Menu
from coffee_maker import CoffeeMaker
from cash_register import CashRegister

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
    cash_register = CashRegister()
    ordered_drink = selected_drink.menu_selection()  # returns a drink
    drink_to_make = is_drink_available(ordered_drink)

    if ordered_drink == "latte" or drink_to_make is not None:
        print(f"{ordered_drink}\t\t ${drink_to_make.cost}")
        if coffee_maker.is_resource_sufficient(drink_to_make):
            f"{cash_register.report()}\n"
        if cash_register.make_payment(drink_to_make.cost):
            coffee_maker.make_coffee(drink_to_make)
            f"{cash_register.report()}\n"
    elif ordered_drink == "espresso" or drink_to_make is not None:
        print(f"{ordered_drink}\t\t ${drink_to_make.cost}")
        if coffee_maker.is_resource_sufficient(drink_to_make):
            f"{cash_register.report()}\n"
        if cash_register.make_payment(drink_to_make.cost):
            coffee_maker.make_coffee(drink_to_make)
            f"{cash_register.report()}\n"
    elif ordered_drink == "cappuccino":
        print(f"{ordered_drink}\t\t ${drink_to_make.cost}")
        if coffee_maker.is_resource_sufficient(drink_to_make):
            f"{cash_register.report()}\n"
        if cash_register.make_payment(drink_to_make.cost):
            coffee_maker.make_coffee(drink_to_make)
            f"{cash_register.report()}\n"
    else:
        ...


if __name__ == '__main__':
    menu_selection()
    process_order()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
