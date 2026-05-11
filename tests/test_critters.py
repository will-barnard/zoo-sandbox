import unittest
from critter import Critter, CritterType

class TestCritter(unittest.TestCase):

    def test_critter_initialization(self):
        critter = Critter(CritterType.BUG)
        self.assertEqual(critter.type, CritterType.BUG)
        self.assertGreaterEqual(critter.health, 0)
        self.assertGreaterEqual(critter.energy, 0)

    def test_critter_eat(self):
        critter = Critter(CritterType.BUG)
        initial_energy = critter.energy
        critter.eat()
        self.assertGreater(critter.energy, initial_energy)

    def test_critter_reproduce(self):
        critter = Critter(CritterType.BUG)
        offspring = critter.reproduce()
        self.assertIsInstance(offspring, Critter)
        self.assertEqual(offspring.type, critter.type)

    def test_critter_die(self):
        critter = Critter(CritterType.BUG)
        critter.health = 0
        critter.die()
        self.assertFalse(critter.alive)

    def test_critter_move(self):
        critter = Critter(CritterType.BUG)
        initial_position = critter.position
        critter.move()
        self.assertNotEqual(critter.position, initial_position)

class TestEmergentGameplay(unittest.TestCase):

    def test_population_growth(self):
        # Assuming a simple model where each critter reproduces once
        initial_population = [Critter(CritterType.BUG) for _ in range(5)]
        for critter in initial_population:
            new_critter = critter.reproduce()
            initial_population.append(new_critter)
        self.assertEqual(len(initial_population), 10)

    def test_resource_consumption(self):
        # Assuming each critter consumes a resource that decreases over time
        resource_amount = 100
        critters = [Critter(CritterType.BUG) for _ in range(5)]
        for critter in critters:
            critter.eat()
            resource_amount -= 1
        self.assertEqual(resource_amount, 95)

if __name__ == '__main__':
    unittest.main()
