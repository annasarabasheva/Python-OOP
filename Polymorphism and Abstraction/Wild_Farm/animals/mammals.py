from Wild_Farm.animals.animal import Mammal
from Wild_Farm.food import Food


class Mouse(Mammal):
    def make_sound(self):
        return "Squeak"

    def feed(self, food: Food):

        if food.__class__.__name__ == "Vegetable" or food.__class__.__name__ == "Fruit":
            self.weight += 0.10 * food.quantity
            self.food_eaten += food.quantity

        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


class Dog(Mammal):
    def make_sound(self):
        return "Woof!"

    def feed(self, food: Food):
        if food.__class__.__name__ == "Meat":
            self.weight += 0.40 * food.quantity
            self.food_eaten += food.quantity

        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


class Cat(Mammal):
    def make_sound(self):
        return "Meow"

    def feed(self, food: Food):
        if food.__class__.__name__ == "Meat" or food.__class__.__name__ == "Vegetable":
            self.weight += 0.30 * food.quantity
            self.food_eaten += food.quantity

        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


class Tiger(Mammal):
    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food: Food):
        if food.__class__.__name__ == "Meat":
            self.weight += 1 * food.quantity
            self.food_eaten += food.quantity

        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
