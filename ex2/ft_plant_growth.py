# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_plant_growth.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: fschnorr <fschnorr@student.42berlin.de>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/20 13:03:21 by fschnorr            #+#    #+#            #
#   Updated: 2026/02/20 15:40:12 by fschnorr           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    def __init__(self, name: str, height_cm: int, age_days: int) -> None:
        self.name = name
        self.height_cm = height_cm
        self.height_start = height_cm
        self.age_days = age_days

    def grow(self) -> None:
        self.height_cm += 1

    def age(self) -> None:
        self.age_days += 1

    def get_info(self) -> str:
        return f"{self.name}: {self.height_cm}cm, {self.age_days} days old"


if __name__ == "__main__":
    plants = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120)
    ]
    print("=== Day 1 ===")
    for plant in plants:
        print(plant.get_info())
    for _ in range(2, 8):
        for plant in plants:
            plant.grow()
            plant.age()
    print("=== Day 7 ===")
    for plant in plants:
        print(plant.get_info())
        growth = plant.height_cm - plant.height_start
        print(f"Growth this week: +{growth}cm")
