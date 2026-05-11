class Critter:
    def __init__(self, name, income):
        self.name = name
        self.generation = 0
        self.income = income

    def generate_income(self):

    def __repr__(self):
        return f"Critter(name={self.name}, income={self.income})"

    @classmethod
    def mate(cls, parent1, parent2):
        new_name = f"{parent1.name}-{parent2.name}"
        new_income = (parent1.income + parent2.income) / 2 + cls._mutate_income()
        offspring = cls(new_name, new_income)
        offspring.generation = max(parent1.generation, parent2.generation) + 1
        return offspring

    @staticmethod
    def _mutate_income():
        import random
        # Simple mutation that can increase or decrease income by up to 5%
        return random.uniform(-0.05, 0.05)
