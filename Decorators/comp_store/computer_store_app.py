from Computer_store.computer_types.desktop_computer import DesktopComputer
from Computer_store.computer_types.laptop import Laptop


class ComputerStoreApp:
    def __init__(self):
        self.warehouse = []  # will store the built computers
        self.profits = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        valid_computers = ["Desktop Computer", "Laptop"]
        result = ""
        if type_computer not in valid_computers:
            raise ValueError(f"{type_computer} is not a valid type computer!")
        if type_computer == "Desktop Computer":
            type_computer = DesktopComputer(manufacturer, model)
        elif type_computer == "Laptop":
            type_computer = Laptop(manufacturer, model)

        result = type_computer.configure_computer(processor, ram)
        self.warehouse.append(type_computer)
        return result

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        for computer in self.warehouse.copy():
            if computer.price <= client_budget and computer.processor == wanted_processor and computer.ram >= wanted_ram:
                profit = client_budget - computer.price
                self.profits += profit
                self.warehouse.remove(computer)
                return f"{computer.__str__()} sold for {client_budget}$."

        raise Exception("Sorry, we don't have a computer for you.")
