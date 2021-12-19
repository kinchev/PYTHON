class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception("Not enough energy.")
        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


import unittest


class WorkerTests(unittest.TestCase):
    def setUp(self):
        self.worker = Worker("Test", 100, 10)

    def test_person_is_initialised_correctly(self):
        worker = Worker("Test", 100, 10)
        self.assertEqual("Test", self.worker.name)
        self.assertEqual(100, worker.salary )
        self.assertEqual(10, worker.energy)
        self.assertEqual(0, worker.money)

    def test_energy_increased_after_reset(self):
        worker = Worker("Test", 100, 10)

        worker.rest()

        self.assertEqual(11, worker.energy)

    def test_error_is_raised_if_the_worker_energy_is_zero_or_negative(self):
        worker = Worker("Test", 100, 0)
        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_increase_worker_money_when_method_is_called(self):
        worker = Worker("Test", 100, 5)
        worker.money = 100
        # self.assertEqual(100,worker.money)
        worker.work()

        self.assertEqual(200, worker.money)

    def test_worker_energy_decrease_when_method_is_called(self):
        worker = Worker("Test", 100, 5)

        worker.work()

        self.assertEqual(4, worker.energy)

    def test_get_info_returns_proper_str_and_value(self):
        worker = Worker("Test", 100, 5)
        worker.money = 100

        self.assertTrue('Test has saved 200 money.', worker.get_info())


if __name__ == "__main__":
    unittest.main()
