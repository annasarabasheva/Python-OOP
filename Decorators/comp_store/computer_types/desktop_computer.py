from Computer_store.computer_types.computer import Computer


class DesktopComputer(Computer):
    def configure_computer(self, processor: str, ram: int):
        available_processors = {"AMD Ryzen 7 5700G": 500, "Intel Core i5-12600K": 600, "Apple M1 Max": 1800}
        if processor not in available_processors:
            raise ValueError(f"{processor} is not compatible with desktop computer {self.manufacturer} {self.model}!")

        valid_ram_sizes = [2 ** i for i in range(1, 8)]

        if ram not in valid_ram_sizes:
            raise ValueError(f"{ram}GB RAM is not compatible with desktop computer {self.manufacturer} {self.model}!")
        ram_price = 0
        for i in range(1, 8):
            if 2 ** i == ram:
                ram_price = i * 100
        computer_price = available_processors[processor] + ram_price

        self.ram = ram
        self.processor = processor
        self.price = computer_price

        return f"Created {self.manufacturer} {self.model} with {processor} and {ram}GB RAM for {computer_price}$."