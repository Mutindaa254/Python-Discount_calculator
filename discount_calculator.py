def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    
    Parameters:
    - price (float): Original price of the item
    - discount_percent (float): Discount percentage to apply

    Returns:
    - float: Final price after discount, or original price if discount < 20%
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount = float(input("Enter the discount percentage: "))

    # Call the function
    final = calculate_discount(original_price, discount)

    # Display result
    if discount >= 20:
        print(f"Discount applied. Final price: ${final:.2f}")
    else:
        print(f"No discount applied. Final price remains: ${final:.2f}")

except ValueError:
    print("Invalid input. Please enter numeric values only.")
