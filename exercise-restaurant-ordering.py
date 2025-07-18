# create a dictionary of menu items and prices
menu_items = {"Burger": 5.99,
            "Pizza": 8.49,
            "Salad": 4.99,
            "Drink": 1.99,}

print("Welcome to the Restaurant Ordering System")

# create a for loop to display menu items and prices
print("Menu:")
for item, price in menu_items.items():
    print(f"{item}: ${price:.2f}")















'''# Create function to calculate total
def calculate_total(order, menu):
    total = 0
    for item, quantity in order.items():
        item_total = menu[item] * quantity
        total = total + item_total

    return round(total, 2) # returning the total rounded to two decimal places'''

