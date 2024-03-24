from meal_menu_unfinished.booths.open_booth import OpenBooth
from meal_menu_unfinished.booths.private_booth import PrivateBooth
from meal_menu_unfinished.delicacies.gingerbread import Gingerbread
from meal_menu_unfinished.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        for delicacy in self.delicacies:
            if delicacy.name == name:
                raise Exception(f"{name} already exists!")
        if type_delicacy not in ["Gingerbread", "Stolen"]:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")
        if type_delicacy == "Gingerbread":
            delicacy = Gingerbread(name, price)
            self.delicacies.append(delicacy)
        elif type_delicacy == "Stolen":
            delicacy = Stolen(name, price)
            self.delicacies.append(delicacy)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        for booth in self.booths:
            if booth.booth_number == booth_number:
                raise Exception(f"Booth number {booth_number} already exists!")
        if type_booth not in ["Open Booth", "Private Booth"]:
            raise Exception(f"{type_booth} is not a valid booth!")
        if type_booth ==  "Open Booth":
            booth = OpenBooth(booth_number, capacity)
            self.booths.append(booth)
        elif type_booth == "Private Booth":
            booth = PrivateBooth(booth_number, capacity)
            self.booths.append(booth)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        for booth in self.booths:
            if not booth.is_reserved and booth.capacity >= number_of_people:
                booth.reserve(number_of_people)
                return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

        raise Exception(f"No available booth for {number_of_people} people!")

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        booth_list = []
        for booth in self.booths:
            if booth.booth_number == booth_number:
                booth_list.append(booth)
        if not booth_list:
            raise Exception(f"Could not find booth {booth_number}!")
        delicacy_list = []
        for delicacy in self.delicacies:
            if delicacy.name == delicacy_name:
                delicacy_list.append(delicacy)
        if not delicacy_list:
            raise Exception(f"No {delicacy_name} in the pastry shop!")
        booth = booth_list[0]
        delicacy = delicacy_list[0]
        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = [b for b in self.booths if b.booth_number == booth_number][0]
        bill = booth.price_for_reservation
        for delicacy in booth.delicacy_orders:
            bill += delicacy.price
        self.income += bill
        booth.delicacy_orders.clear()
        booth.is_reserved = False
        booth.price_for_reservation = 0
        return f"Booth {booth_number}:\nBill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."






