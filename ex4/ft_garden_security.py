# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_garden_security.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: fschnorr <fschnorr@student.42berlin.de>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/20 15:44:13 by fschnorr            #+#    #+#            #
#   Updated: 2026/02/23 14:39:32 by fschnorr           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class SecurePlant:
    def __init__(self, name: str) -> None:
        self.name = name
        self._height_cm = 0
        self._age_days = 0
        self.get_created_line()

    def set_height(self, height_cm: int) -> None:
        if height_cm < 0:
            print(
                "\nInvalid operation attempted: height "
                f"{height_cm}cm [REJECTED]"
                "\nSecurity: Negative height rejected")
        else:
            self._height_cm = height_cm
            print(f"Height updated: {height_cm}cm [OK]")

    def set_age(self, age_days: int) -> None:
        if age_days < 0:
            print(
                "\nInvalid operation attempted: age "
                f"{age_days} days [REJECTED]"
                "\nSecurity: Negative age rejected")
        else:
            self._age_days = age_days
            print(f"Age updated: {age_days} days [OK]")

    def get_height(self) -> int:
        return self._height_cm

    def get_age(self) -> int:
        return self._age_days

    def get_created_line(self) -> None:
        print(f"Plant created: {self.name}")

    def get_info(self) -> str:
        return f"{self.name} ({self.get_height()}cm, {self.get_age()} days)"


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant_data = [
        ("Rose"),
    ]
    plants = []
    for name in plant_data:
        plants.append(SecurePlant(name))

    plants[0].set_height(25)
    plants[0].set_age(30)
    plants[0].set_height(-5)
    print(f"\nCurrent plant: {plants[0].get_info()}")
