from robot_service.robots.female_robot import FemaleRobot
from robot_service.robots.male_robot import MaleRobot
from robot_service.services.main_service import MainService
from robot_service.services.secondary_service import SecondaryService


class RobotsManagingApp:
    def __init__(self):
        self.robots = []
        self.services = []

    def add_service(self, service_type: str, name: str):
        if service_type not in ["MainService", "SecondaryService"]:
            raise Exception("Invalid service type!")
        if service_type == "MainService":
            service = MainService(name)
            self.services.append(service)
        elif service_type == "SecondaryService":
            service = SecondaryService(name)
            self.services.append(service)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in ["MaleRobot", "FemaleRobot"]:
            raise Exception("Invalid robot type!")
        if robot_type == "MaleRobot":
            robot = MaleRobot(name, kind, price)
            self.robots.append(robot)
        elif robot_type == "FemaleRobot":
            robot = FemaleRobot(name, kind, price)
            self.robots.append(robot)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = [r for r in self.robots if r.name == robot_name][0]
        service = [s for s in self.services if s.name == service_name][0]
        if robot.__class__.__name__ == "FemaleRobot" and service.__class__.__name__ == "SecondaryService":
            if len(service.robots) < service.capacity:
                self.robots.remove(robot)
                service.robots.append(robot)
                return f"Successfully added {robot_name} to {service_name}."
            else:
                raise Exception("Not enough capacity for this robot!")
        elif robot.__class__.__name__ == "MaleRobot" and service.__class__.__name__ == "MainService":
            if len(service.robots) < service.capacity:
                self.robots.remove(robot)
                service.robots.append(robot)
                return f"Successfully added {robot_name} to {service_name}."
            else:
                raise Exception("Not enough capacity for this robot!")
        return "Unsuitable service."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = [s for s in self.services if s.name == service_name][0]
        for robot in service.robots.copy():
            if robot.name == robot_name:
                service.robots.remove(robot)
                self.robots.append(robot)
                # service.capacity += 1
                return f"Successfully removed {robot_name} from {service_name}."
        raise Exception("No such robot in this service!")

    def feed_all_robots_from_service(self, service_name: str):
        service = [s for s in self.services if s.name == service_name][0]
        for robot in service.robots:
            robot.eating()
        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name: str):
        service = [s for s in self.services if s.name == service_name][0]
        price = 0
        for robot in service.robots:
            price += robot.price
        return f"The value of service {service_name} is {price:.2f}."

    def __str__(self):
        result = ""
        for service in self.services:
            result += f"{service.details()}\n"

        result = result.rstrip()
        return result
