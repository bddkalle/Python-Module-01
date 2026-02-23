# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_garden_intro.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: fschnorr <fschnorr@student.42berlin.de>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/19 15:50:31 by fschnorr            #+#    #+#            #
#   Updated: 2026/02/20 12:55:42 by fschnorr           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def show_plant() -> None:
    name = "Rose"
    height = "25cm"
    age = "30 days"
    print("=== Welcome to My Garden ===")
    print(f"Plant: {name}")
    print(f"Height: {height}")
    print(f"Age: {age}")
    print("\n=== End of Program ===")


if __name__ == "__main__":
    show_plant()
