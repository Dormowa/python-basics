# Set up product menu
items = {"Cleanser": 10.00,
            "Toner": 15.00,
            "Hyaluronic acid": 20.00,
            "Niacinamide": 25.00,
            "Vitamin C Serum": 30.00,
            "Sunscreen": 45.00,
            "Night Cream": 100.00}
print(items)

# Prompt for initial funds
funds = float(input("How much money are you inserting into the machine? $"))

# Display the item and price list
for product, price in items.items():
    print(f"{product:<20} ${price:.2f}")
 
# Start transaction while loop
while funds > 0:
    print(f"\nCurrent balance: ${funds:.2f}")

# User selects an item
    choice = input("Enter the name of the item you want to purchase: ").strip()

# If the item is not found
    if choice not in items:
        print("Item not found.")
        continue

    elif funds >= items[choice]:
        price = items[choice]
        funds -= price
        print(f"{choice} dispensed.")
        print(f"Remaining balance: ${funds:.2f}")
    else:
        print(f"Insufficient funds for {choice}.")
        more = input("Do you want to add more money? (yes/no): ").lower()
        if more == "yes":
            extra = float(input("Enter amount to add: $"))
            funds += extra
            continue
        else:
            print("Transaction cancelled.")
            break

    again = input("Do you want to make another purchase? (yes/no): ").lower()
    if again != "yes":
     print("Thank you for your purchase. Goodbye.")
     break