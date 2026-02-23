# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_garden_data.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: fschnorr <fschnorr@student.42berlin.de>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/20 13:03:21 by fschnorr            #+#    #+#            #
#   Updated: 2026/02/20 13:35:56 by fschnorr           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    def __init__(self, name: str, height_cm: int, age_days: int) -> None:
        self.name = name
        self.height_cm = height_cm
        self.age_days = age_days


def show_plant(plant: Plant) -> None:
    print(f"{plant.name}: {plant.height_cm}cm, {plant.age_days} days old")


if __name__ == "__main__":
    plant0 = Plant("Rose", 25, 30)
    plant1 = Plant("Sunflower", 80, 45)
    plant2 = Plant("Cactus", 15, 120)
    plants = [plant0, plant1, plant2]
    print("=== Garden Plant Registry ===")
    for i in range(3):
        show_plant(plants[i])
