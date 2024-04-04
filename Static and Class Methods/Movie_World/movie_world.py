from Movie_World.customer import Customer
from Movie_World.dvd import DVD


class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = [] #Customer objects
        self.dvds = [] # dvds objects

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < 10:
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < 15:
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        for customer in self.customers:
            if customer.id == customer_id:
                for dvd in self.dvds:
                    if dvd.id == dvd_id:
                        if dvd in customer.rented_dvds:
                            return f"{customer.name} has already rented {dvd.name}"

                        elif dvd not in customer.rented_dvds and dvd.is_rented:
                            return "DVD is already rented"

                        elif dvd not in customer.rented_dvds and customer.age < dvd.age_restriction:
                            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

                        customer.rented_dvds.append(dvd)
                        dvd.is_rented = True
                        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        for customer in self.customers:
            if customer.id == customer_id:
                for dvd in self.dvds:
                    if dvd.id == dvd_id:
                        if dvd in customer.rented_dvds:
                            customer.rented_dvds.remove(dvd)
                            dvd.is_rented = False
                            return f"{customer.name} has successfully returned {dvd.name}"

                        return f"{customer.name} does not have that DVD"

    def __repr__(self):
        result = ""
        for customer in self.customers:
            result += f"{customer}\n"

        for dvd in self.dvds:
            result += f"{dvd}\n"

        return result





