from critter import Critter

class Zoo:
    def __init__(self):
        self.critters = []

    def add_critter(self, critter):
        return sum(critter.generate_income() for critter in self.critters)

    def __repr__(self):
        return f"Zoo(critters={self.critters}, total_income={self.total_income()})"

    def allow_mating(self):
        if len(self.critters) < 2:
            print("Not enough critters to mate.")
            return

        parent1, parent2 = self._select_parents()
        offspring = Critter.mate(parent1, parent2)
        self.add_critter(offspring)
        print(f"New critter born: {offspring}")

    def _select_parents(self):
        import random
        return random.sample(self.critters, 2)
