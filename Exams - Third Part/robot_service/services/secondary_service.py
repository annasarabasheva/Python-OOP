from robot_service.services.base_service import BaseService


class SecondaryService(BaseService):
    def __init__(self, name):
        super().__init__(name, capacity=15)

    def details(self):
        if not self.robots:
            return f"{self.name} Secondary Service:\nRobots: none"
        robot_names = []
        for robot in self.robots:
            robot_names.append(robot.name)
        return f"{self.name} Secondary Service:\nRobots: {' '.join(robot_names)}"

