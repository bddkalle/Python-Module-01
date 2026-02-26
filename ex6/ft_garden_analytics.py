# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_garden_analytics.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: fschnorr <fschnorr@student.42berlin.de>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/20 15:44:13 by fschnorr            #+#    #+#            #
#   Updated: 2026/02/24 23:00:08 by fschnorr           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    def __init__(self, name: str, height_cm: int) -> None:
        self.name = name
        self._height_cm = 0
        self.set_height(height_cm)
        self.start_height_cm = self.get_height()

    def set_height(self, height_cm: int) -> None:
        if height_cm < 0:
            print(
                "\nInvalid operation attempted: height "
                f"{height_cm}cm [REJECTED]"
                "\nSecurity: Negative height rejected")
        else:
            self._height_cm = height_cm

    def get_height(self) -> int:
        return self._height_cm

    def get_created_line(self) -> None:
        print(f"Plant created: {self.name}")

    def get_info(self) -> str:
        return f"- {self.name}: {self.get_height()}cm"

    def get_type(self) -> str:
        return "regular"

    def get_score(self) -> int:
        return self.get_height()


class FloweringPlant(Plant):
    def __init__(self, name: str, height_cm: int, color: str) -> None:
        super().__init__(name, height_cm)
        self.color = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")

    def get_info(self) -> str:
        return (
            f"- {self.name}: {self.get_height()}cm, "
            f"{self.color} flowers (blooming)")

    def get_type(self) -> str:
        return "flowering"

    def get_score(self) -> int:
        return self.get_height() + 20


class PrizeFlower(FloweringPlant):
    def __init__(
            self, name: str, height_cm: int, color: str, prize_points: int
            ) -> None:
        super().__init__(name, height_cm, color)
        self._prize_points = 0
        self.set_prize_points(prize_points)

    def get_info(self) -> str:
        return (
            f"- {self.name}: {self.get_height()}cm, "
            f"{self.color} flowers (blooming), Prize points: "
            f"{self.get_prize_points()}")

    def set_prize_points(self, prize_points: int) -> None:
        if prize_points < 0:
            print(
                "\nInvalid operation attempted: prize points "
                f"{prize_points} [REJECTED]"
                "\nSecurity: Negative prize points rejected")
        else:
            self._prize_points = prize_points

    def get_prize_points(self) -> int:
        return self._prize_points

    def get_type(self) -> str:
        return "prize"

    def get_score(self) -> int:
        return self.get_height() + 10 + self.get_prize_points()


class GardenManager:
    total_gardens_managed = 0

    class GardenStats:
        @staticmethod
        def count_plants(plants: list[Plant]) -> int:
            count = 0
            for _ in plants:
                count += 1
            return count

        @staticmethod
        def calc_growth(plants: list[Plant]) -> int:
            growth = 0
            for plant in plants:
                growth += plant.get_height() - plant.start_height_cm
            return growth

        @staticmethod
        def count_types(plants: list[Plant]) -> tuple[int, int, int]:
            regular = 0
            flowering = 0
            prize = 0
            for plant in plants:
                plant_type = plant.get_type()
                if plant_type == "prize":
                    prize += 1
                elif plant_type == "flowering":
                    flowering += 1
                else:
                    regular += 1
            return (regular, flowering, prize)

        @staticmethod
        def validate_height(plants: list[Plant]) -> bool:
            for plant in plants:
                if plant.get_height() < 0:
                    return False
            return True

    def __init__(self, owner_name: str) -> None:
        self.owner_name = owner_name
        self.plants = []
        GardenManager.total_gardens_managed += 1

    def add_plant(self, plant: Plant, announce: bool = True) -> None:
        self.plants.append(plant)
        if announce:
            print(f"Added {plant.name} to {self.owner_name}'s garden")

    def help_plants_grow(self) -> None:
        print(f"\n{self.owner_name} is helping all plants grow...")
        for plant in self.plants:
            plant.set_height(plant.get_height() + 1)
            print(f"{plant.name} grew 1cm")

    def print_report(self) -> None:
        print(f"\n=== {self.owner_name}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(plant.get_info())

        regular, flowering, prize = self.GardenStats.count_types(self.plants)
        print(
            f"\nPlants added: {self.GardenStats.count_plants(self.plants)}, "
            f"Total growth: {self.GardenStats.calc_growth(self.plants)}cm\n"
            f"Plant types: {regular} regular, {flowering} flowering, "
            f"{prize} prize flowers")
        print(
            f"\nHeight validation test: "
            f"{self.GardenStats.validate_height(self.plants)}")

    def calculate_garden_score(self) -> int:
        score = 0
        for plant in self.plants:
            score += plant.get_score()
        return score

    @classmethod
    def get_total_gardens(cls) -> int:
        return cls.total_gardens_managed

    @classmethod
    def create_garden_network(
            cls, owner_names: list[str]) -> list["GardenManager"]:
        managers = []
        for owner_name in owner_names:
            managers.append(cls(owner_name))
        return managers


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")

    network = GardenManager.create_garden_network(["Alice", "Bob"])
    alice_manager = network[0]
    bob_manager = network[1]
    # alice_manager = GardenManager("Alice")
    # bob_manager = GardenManager("Bob")

    alice_manager.add_plant(Plant("Oak Tree", 100))
    alice_manager.add_plant(FloweringPlant("Rose", 25, "red"))
    alice_manager.add_plant(PrizeFlower("Sunflower", 50, "yellow", 10))

    bob_manager.add_plant(Plant("Mint", 50), announce=False)
    bob_manager.add_plant(Plant("Basil", 42), announce=False)

    alice_manager.help_plants_grow()

    alice_manager.print_report()
    print(
        f"Garden scores - Alice: "
        f"{alice_manager.calculate_garden_score()}, "
        f"Bob: {bob_manager.calculate_garden_score()}")
    print(f"Total gardens managed: {GardenManager.get_total_gardens()}")
