# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_plant_factory.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: fschnorr <fschnorr@student.42berlin.de>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/20 15:44:13 by fschnorr            #+#    #+#            #
#   Updated: 2026/02/23 13:40:42 by fschnorr           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    def __init__(self, name: str, height_cm: int, age_days: int) -> None:
        self.name = name
        self.height_cm = height_cm
        self.age_days = age_days

    def get_created_line(self) -> None:
        print(
            f"Created: {self.name} "
            f"({self.height_cm}cm, {self.age_days} days)")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    plant_data = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
    ]
    plants = []
    for name, height_cm, age_days in plant_data:
        plants.append(Plant(name, height_cm, age_days))
    count = 0
    for plant in plants:
        plant.get_created_line()
        count += 1
    print(f"\nTotal plants created: {count}")
