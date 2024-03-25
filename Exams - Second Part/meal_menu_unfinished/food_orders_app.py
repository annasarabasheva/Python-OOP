from meal_menu_unfinished.client import Client
from meal_menu_unfinished.meals.meal import Meal


class FoodOrdersApp:
    def __init__(self):
        self.menu = []
        self.clients_list = []

    def register_client(self, client_phone_number: str):
        for client in self.clients_list:
            if client.phone_number == client_phone_number:
                raise Exception("The client has already been registered!")

        client = Client(client_phone_number)
        self.clients_list.append(client)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if meal.__class__.__name__ in ["Starter", "MainDish", "Dessert"]:
                self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
        for meal in self.menu:
            meal.details()

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        client_in_list = []
        for client in self.clients_list:
            if client.phone_number == client_phone_number:
                client_in_list.append(client)
        if not client_in_list:
            client = Client(client_phone_number)
            self.clients_list.append(client)
        else:
            client = client_in_list[0]
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
        all_meal_names_in_menu = []
        for meal in self.menu:
            all_meal_names_in_menu.append(meal.name)
        for meal_name, quantity in meal_names_and_quantities.items():
            meal = [meal for meal in self.menu if meal.name == meal_name][0]
            if meal_name not in all_meal_names_in_menu:
                client.shopping_cart.clear()
                client.bill = 0
                raise Exception(f"{meal_name} is not on the menu!")
            if meal.quantity < quantity:
                client.shopping_cart.clear()
                client.bill = 0
                raise Exception(f"Not enough quantity of {meal.__class__.__name__}: {meal_name}!")
            client.shopping_cart.append(meal)
            client.bill += (meal.price * quantity)
            meal.quantity -= quantity

        shopping_cart_names = [meal.name for meal in client.shopping_cart]
        return f"Client {client_phone_number} successfully ordered {', '.join(shopping_cart_names)} for {client.bill:.2f}lv."


    def cancel_order(self, client_phone_number: str):
        pass













