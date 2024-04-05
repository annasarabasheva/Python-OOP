class Worker:
    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')
        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'



import unittest


class WorkerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.worker = Worker("Matt", 5000, 100)

    def test_initialization_of_attributes(self):
        self.assertEqual(self.worker.name, "Matt")
        self.assertEqual(self.worker.salary, 5000)
        self.assertEqual(self.worker.energy, 100)
        self.assertEqual(self.worker.money, 0)

    def test_working_when_energy_is_zero(self):
        worker = Worker("Matt", 5000, 0)
        self.assertEqual(worker.energy, 0)

        with self.assertRaises(Exception) as ex:
            worker.work()

        self.assertEqual(str(ex.exception), "Not enough energy.")

    def test_working_when_energy_is_minus(self):
        worker = Worker("Matt", 5000, -1)
        self.assertEqual(worker.energy, -1)

        with self.assertRaises(Exception) as ex:
            worker.work()

        self.assertEqual(str(ex.exception), "Not enough energy.")

    def test_working_and_increasing_money(self):
        self.assertEqual(self.worker.money, 0)
        self.assertEqual(self.worker.salary, 5000)

        self.worker.work()
        self.assertEqual(self.worker.money, 5000)

        self.worker.work()
        self.assertEqual(self.worker.money, 10000)

    def test_working_and_decreasing_energy(self):
        self.assertEqual(self.worker.energy, 100)

        self.worker.work()
        self.assertEqual(self.worker.energy, 99)

        self.worker.work()
        self.assertEqual(self.worker.energy, 98)

    def test_resting(self):
        self.assertEqual(self.worker.energy, 100)
        self.worker.rest()
        self.assertEqual(self.worker.energy, 101)

        self.worker.rest()
        self.assertEqual(self.worker.energy, 102)

    def test_get_info(self):
        result = self.worker.get_info()
        self.assertEqual(result,'Matt has saved 0 money.')


if __name__ == "__main__":
    unittest.main()