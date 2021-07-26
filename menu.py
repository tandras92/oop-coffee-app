from art import logo
from os import system
from os import name as os_name


def clear():
    if os_name == "nt":  # For Windows OS
        _ = system("cls")
    else:
        _ = system("clear")


class MenuItem:
    """Models each Menu Item."""

    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {"water": water, "milk": milk, "coffee": coffee}


class Menu:
    """Models the Menu with drinks."""

    def __init__(self):
        self.logo = logo
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]
        self.options = {
            "1": "View Menu",
            "2": "Search Drinks",
            "3": "Print Receipt",
            "4": "Quit",
        }

    @staticmethod
    def print_menu_banner():
        print("========= Welcome to the Coffee Shop Program =========")
        center_logo = logo.center(20)
        print(center_logo)

    def get_items(self):
        """Returns all the names of the available menu items"""
        options = ""
        option_number = 1
        for item in self.menu:
            options += f"{str(option_number)}. {item.name}\n"
            option_number += 1
        return options

    def find_drink(self, order_name):
        """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")

    def menu_selection(self):
        print("Please select from the following options:")
        menu_options = self.options
        menu_items = self.get_items()
        for k, v in menu_options.items():
            print(f"{k}. {v}")
        user_selection = input("\nSelection: ")
        clear()  # clears the terminal
        # TODO - add try/except and logs
        for option in menu_options:
            if option == "1" and option == user_selection:
                print("Please Select a Beverage:")
                print(menu_items)
                beverage_choice = input("\nSelection: ")
                for drink_option in menu_items:
                    if drink_option == "1" and drink_option == beverage_choice:
                        ...
            elif option == "2" and option == user_selection:
                order_name = input("Please enter the name of drink: ")
                self.find_drink(order_name)
            elif option == "3" and option == user_selection:
                ...
            elif option == "4" and option == user_selection:
                ...
            else:
                ...
