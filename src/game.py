import time

class ZooGame:
    UPGRADES = {'capacity': (100, 20), 'happiness': (50, 5)}
    def __init__(self):
        self.critters = []
        self.income = 0
            print(f"{critter.name} is {critter.happiness}% happy.")
            time.sleep(1)

    def show_upgrades(self):
        print("Available Upgrades:")
        for upgrade, (cost, benefit) in self.UPGRADES.items():
            if self.income >= cost:
                print(f"- {upgrade.capitalize()}: +{benefit} (Cost: {cost})")

    def apply_upgrade(self, upgrade):
        if upgrade not in self.UPGRADES:
            print("Invalid upgrade.")
            return

        cost, benefit = self.UPGRADES[upgrade]
        if self.income < cost:
            print("Not enough income to purchase this upgrade.")
            return

        self.income -= cost
        if upgrade == 'capacity':
            self.capacity += benefit
        elif upgrade == 'happiness':
            for critter in self.critters:
                critter.happiness = min(100, critter.happiness + benefit)
        print(f"Upgrade {upgrade.capitalize()} applied successfully.")

    def main_menu(self):
        while True:
            print("\nMain Menu:")
                self.add_critter()
            elif choice == '3':
                self.collect_income()
            elif choice == '4':
                self.show_upgrades()
                upgrade = input("Enter the upgrade to purchase: ").strip().lower()
                self.apply_upgrade(upgrade)
            elif choice == '5':
                print("Exiting game.")
                break
