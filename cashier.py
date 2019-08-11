def get_order(order):
    rest_dict = ["Burger", "Fries", "Chicken", "Pizza", "Sandwich", "Onionrings", "Milkshake", "Coke"]
    new_order = []
    for entry in rest_dict:
        new_order.extend([entry for _ in range(order.count(entry.lower()))])
    return " ".join(new_order)



print(get_order("milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza"))
print(get_order("pizzachickenfriesburgercokemilkshakefriessandwich"))

"""
search in string for menu item x
    pop matching item
    perform steps: Capitalize, Split with space
"""