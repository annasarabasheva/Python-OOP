from Wild_Cat_Zoo.animal import Animal
from Wild_Cat_Zoo.caretaker import Caretaker
from Wild_Cat_Zoo.cheetah import Cheetah
from Wild_Cat_Zoo.keeper import Keeper
from Wild_Cat_Zoo.lion import Lion
from Wild_Cat_Zoo.tiger import Tiger
from Wild_Cat_Zoo.vet import Vet
from Wild_Cat_Zoo.worker import Worker


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if self.__budget >= price and self.__animal_capacity > 0:
            self.animals.append(animal)
            self.__budget -= price
            self.__animal_capacity -= 1
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        elif self.__budget < price and self.__animal_capacity > 0:
            return "Not enough budget"

        return f"Not enough space for animal"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity > 0:
            self.workers.append(worker)
            #self.__workers_capacity -= 1
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                #self.__workers_capacity += 1
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salary = 0
        for worker in self.workers:
            total_salary += worker.salary

        if self.__budget >= total_salary:
            self.__budget -= total_salary
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_care_money = 0
        for animal in self.animals:
            total_care_money += animal.money_for_care

        if self.__budget >= total_care_money:
            self.__budget -= total_care_money
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = 0
        tigers = 0
        cheetah = 0
        result_one = ''
        for animal in self.animals:
            if animal.__class__.__name__ == "Lion":
                lions += 1
                result_one += f"{animal.__repr__()}\n"
        result = f"You have {len(self.animals)} animals\n----- {lions} Lions:\n{result_one}"
        result_two = ''
        for animal in self.animals:
            if animal.__class__.__name__ == "Tiger":
                tigers += 1
                result_two += f"{animal.__repr__()}\n"

        result += f'----- {tigers} Tigers:\n{result_two}'
        new_result = ''
        for animal in self.animals:
            if animal.__class__.__name__ == "Cheetah":
                cheetah += 1
                new_result += f"{animal.__repr__()}\n"

        result += f'----- {cheetah} Cheetahs:\n{new_result}'
        result = result.rstrip()
        return result

    def workers_status(self):
        keepers = 0
        caretakers = 0
        vetes = 0
        result_one = ''
        for worker in self.workers:
            if worker.__class__.__name__ == "Keeper":
                keepers += 1
                result_one += f"{worker.__repr__()}\n"
        result = f"You have {len(self.workers)} workers\n----- {keepers} Keepers:\n{result_one}"
        result_two = ''
        for worker in self.workers:
            if worker.__class__.__name__ == "Caretaker":
                caretakers += 1
                result_two += f"{worker.__repr__()}\n"

        result += f'----- {caretakers} Caretakers:\n{result_two}'
        new_result = ''
        for worker in self.workers:
            if worker.__class__.__name__ == "Vet":
                vetes += 1
                new_result += f"{worker.__repr__()}\n"

        result += f'----- {vetes} Vets:\n{new_result}'
        result = result.rstrip()
        return result



zoo = Zoo("Zootopia", 0, 1, 1)
# Animals creation
animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4), Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]
# Animal prices
prices = [200, 190, 204, 156, 211, 140]
# Workers creation

workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68), Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)]
# Adding all animals
"""
for i in range(len(animals)):
    animal = animals[i]
    price = prices[i]
    print(zoo.add_animal(animal, price))
# Adding all workers
for worker in workers:
    print(zoo.hire_worker(worker))
    # Tending animals
print(zoo.tend_animals())
# Paying keepers
print(zoo.pay_workers())
# Fireing worker
print(zoo.fire_worker("Adam"))
# Printing statuses
print(zoo.animals_status())
print(zoo.workers_status())
"""

z = Zoo("Some Zoo", 1500, 1, 1)
print(z.hire_worker(Vet("I am Vet", 20, 500)))
print(len(z.workers))
print(z._Zoo__workers_capacity)