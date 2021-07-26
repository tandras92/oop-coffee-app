from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def start():
    coffee_menu = Menu()
    coffee_menu.print_menu_banner()
    coffee_menu.menu_selection()


if __name__ == '__main__':
    start()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
