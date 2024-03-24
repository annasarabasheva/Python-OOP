from drive.vehicles.base_vehicle import BaseVehicle


class CargoVan(BaseVehicle):
    MAX_MILEAGE = 180.00

    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, max_mileage=CargoVan.MAX_MILEAGE)

    def drive(self, mileage: float):
        percentage_passed = (mileage / self.MAX_MILEAGE) * 100
        battery_reduction = round(percentage_passed + 5)

        self.battery_level -= battery_reduction

