def calculate_bill_with_vat():
    print("Welcome to the Billing System with 13% VAT")
    print("-" * 50)

    # Step 1: Ask how many types of items
    try:
        item_count = int(input("Enter the number of different item types: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    items = []
    total_without_vat = 0

    # Step 2: Loop to take item name, quantity, and cost per piece
    for i in range(item_count):
        print(f"\nItem {i+1}")
        item_name = input("Enter item name (e.g., Biscuit, Oats): ").strip()
        try:
            quantity = int(input(f"Enter quantity of {item_name}: "))
            price_per_unit = float(input(f"Enter price per 1 piece of {item_name}: "))
        except ValueError:
            print("Invalid number! Skipping this item.")
            continue

        amount = quantity * price_per_unit
        total_without_vat += amount
        items.append((item_name, quantity, price_per_unit, amount))

    # Step 3: Calculate 13% VAT and final total
    vat = total_without_vat * 0.13
    total_with_vat = total_without_vat + vat

    # Step 4: Display final bill
    print("\n--- Final Bill ---")
    for idx, (name, qty, price, amt) in enumerate(items, start=1):
        print(f"{idx}. {name}: {qty} pcs x Rs.{price:.2f} = Rs.{amt:.2f}")

    print("-" * 50)
    print(f"Subtotal (without VAT): Rs.{total_without_vat:.2f}")
    print(f"13% VAT: Rs.{vat:.2f}")
    print(f"Total Amount to Pay: Rs.{total_with_vat:.2f}")
    print("Thank you for shopping!")

# Run the program
calculate_bill_with_vat()