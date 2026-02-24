# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_plant_types.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: fschnorr <fschnorr@student.42berlin.de>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/20 15:44:13 by fschnorr            #+#    #+#            #
#   Updated: 2026/02/24 11:15:05 by fschnorr           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    def __init__(self, name: str, height_cm: int, age_days: int) -> None:
        self.name = name
        self._height_cm = 0
        self.set_height(height_cm)
        self._age_days = 0
        self.set_age(age_days)

    def set_height(self, height_cm: int) -> None:
        if height_cm < 0:
            print(
                "\nInvalid operation attempted: height "
                f"{height_cm}cm [REJECTED]"
                "\nSecurity: Negative height rejected")
        else:
            self._height_cm = height_cm
            # print(f"Height updated: {height_cm}cm [OK]")

    def set_age(self, age_days: int) -> None:
        if age_days < 0:
            print(
                "\nInvalid operation attempted: age "
                f"{age_days} days [REJECTED]"
                "\nSecurity: Negative age rejected")
        else:
            self._age_days = age_days
            # print(f"Age updated: {age_days} days [OK]")

    def get_height(self) -> int:
        return self._height_cm

    def get_age(self) -> int:
        return self._age_days

    def get_created_line(self) -> None:
        print(f"Plant created: {self.name}")

    def get_info(self) -> str:
        return f"{self.name} ({self.get_height()}cm, {self.get_age()} days)"


class Flower(Plant):
    def __init__(
        self, name: str, height_cm: int, age_days: int, color: str
    ) -> None:
        super().__init__(name, height_cm, age_days)
        self.color = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")

    def get_info(self) -> str:
        return (
            f"{self.name} (Flower): {self.get_height()}cm, "
            f"{self.get_age()} days, {self.color}")


class Tree(Plant):
    def __init__(
        self, name: str, height_cm: int, age_days: int, trunk_diameter: int
    ) -> None:
        super().__init__(name, height_cm, age_days)
        self._trunk_diameter = 0
        self.set_trunk_diameter(trunk_diameter)

    def produce_shade(self) -> None:
        print(f"{self.name} provides 78 square meters of shade")

    def get_info(self) -> str:
        return (
            f"{self.name} (Tree): {self.get_height()}cm, "
            f"{self.get_age()} days, {self.get_trunk_diameter()}cm diameter")

    def get_trunk_diameter(self) -> int:
        return self._trunk_diameter

    def set_trunk_diameter(self, trunk_diameter: int) -> None:
        if trunk_diameter < 0:
            print(
                "\nInvalid operation attempted: trunk diameter "
                f"{trunk_diameter}cm [REJECTED]"
                "\nSecurity: Negative trunk diameter rejected")
        else:
            self._trunk_diameter = trunk_diameter


class Vegetable(Plant):
    def __init__(
        self, name: str, height_cm: int, age_days: int, harvest_season: str,
        nutritional_value: str
    ) -> None:
        super().__init__(name, height_cm, age_days)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def nutritional_value_info(self) -> None:
        print(f"{self.name} is rich in {self.nutritional_value}")

    def get_info(self) -> str:
        return (
            f"{self.name} (Vegetable): {self.get_height()}cm, "
            f"{self.get_age()} days, {self.harvest_season} harvest")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    flower_data = [
        ("Rose", 25, 30, "red color"),
    ]
    flowers = []
    for name, height_cm, age_days, color in flower_data:
        flowers.append(Flower(name, height_cm, age_days, color))
    for flower in flowers:
        print(f"\n{flower.get_info()}")
        flower.bloom()

    tree_data = [
        ("Oak", 500, 1825, 50),
    ]
    trees = []
    for name, height_cm, age_days, trunk_diameter in tree_data:
        trees.append(Tree(name, height_cm, age_days, trunk_diameter))
    for tree in trees:
        print(f"\n{tree.get_info()}")
        tree.produce_shade()

    vegetable_data = [
        ("Tomato", 80, 90, "summer", "vitamin C"),
    ]
    vegetables = []
    for (
        name, height_cm, age_days, harvest_season, nutritional_value
    ) in vegetable_data:
        vegetables.append(Vegetable(
            name, height_cm, age_days, harvest_season, nutritional_value
            ))
    for vegetable in vegetables:
        print(f"\n{vegetable.get_info()}")
        vegetable.nutritional_value_info()
