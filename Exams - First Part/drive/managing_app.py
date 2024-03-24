from drive.route import Route
from drive.user import User
from drive.vehicles.cargo_van import CargoVan
from drive.vehicles.passenger_car import PassengerCar


class ManagingApp:
    def __init__(self):
        self.users = []  # users (objects) that are created.
        self.vehicles = []  # vehicles (objects) that are created.
        self.routes = []  # routes (objects) that are created.

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        for u in self.users:
            if u.driving_license_number == driving_license_number:
                return f"{driving_license_number} has already been registered to our platform."
        user = User(first_name, last_name, driving_license_number)
        self.users.append(user)
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in ["PassengerCar", "CargoVan"]:
            return f"Vehicle type {vehicle_type} is inaccessible."
        for v in self.vehicles:
            if v.license_plate_number == license_plate_number:
                return f"{license_plate_number} belongs to another vehicle."
        if vehicle_type == "PassengerCar":
            vehicle = PassengerCar(brand, model, license_plate_number)
            self.vehicles.append(vehicle)
        elif vehicle_type == "CargoVan":
            vehicle = CargoVan(brand, model, license_plate_number)
            self.vehicles.append(vehicle)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        for r in self.routes:
            if r.start_point == start_point and r.end_point == end_point and r.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."
            elif r.start_point == start_point and r.end_point == end_point and r.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."
            elif r.start_point == start_point and r.end_point == end_point and r.length > length:
                r.is_locked = True
        route_id = len(self.routes) + 1
        route = Route(start_point, end_point, length, route_id)
        self.routes.append(route)
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,
                  is_accident_happened: bool):
        user = [u for u in self.users if u.driving_license_number == driving_license_number][0]
        vehicle = [v for v in self.vehicles if v.license_plate_number == license_plate_number][0]
        route = [r for r in self.routes if r.route_id == route_id][0]
        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."
        elif vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."
        elif route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."
        vehicle.drive(route.length)
        if is_accident_happened:
            vehicle.is_damaged = True
            user.decrease_rating()
        else:
            user.increase_rating()
        return str(vehicle)

    def repair_vehicles(self, count: int):
        damaged_vehicles = []
        for vehicle in self.vehicles:
            if vehicle.is_damaged:
                damaged_vehicles.append(vehicle)
        if not damaged_vehicles:
            return f"0 vehicles were successfully repaired!"
        sorted_vehicles = sorted(damaged_vehicles, key=lambda v: (v.brand, v.model))
        if count == 0:
            return f"{count} vehicles were successfully repaired!"
        elif count >= len(damaged_vehicles):
            for vehicle in sorted_vehicles:
                vehicle.is_damaged = False
                vehicle.recharge()
            return f"{len(damaged_vehicles)} vehicles were successfully repaired!"
        elif count < len(damaged_vehicles):
            repaired_vehicles = []
            for v in sorted_vehicles:
                repaired_vehicles.append(v)
                count -= 1
                if count == 0:
                    break
            for vehicle in repaired_vehicles:
                vehicle.is_damaged = False
                vehicle.recharge()
            return f"{len(repaired_vehicles)} vehicles were successfully repaired!"

    def users_report(self):
        sorted_users = sorted(self.users, key=lambda u: (-u.rating))
        # result = "*** E-Drive-Rent ***\n"
        result = "*** E-Drive-Rent ***"
        for user in sorted_users:
            # result += f"{str(user)}\n"
            result += f"\n{user.__str__()}"
        return result
