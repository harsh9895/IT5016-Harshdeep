def calculate_total_cost(items):
    total_cost = 0
    for item, price in items:
        total_cost += apply_discount(price)  
    return total_cost

def apply_discount(price):
    if price > 300:
        discount = price * 0.05  
        price -= discount  # Apply discount
    return price

def main():
    # List to store items as tuples (item_name, price)
    shopping_cart = []

    num_items = int(input("How many items did you purchase? "))
    
    for _ in range(num_items):
        item_name = input("Enter the item name: ")
        price = float(input(f"Enter the price for {item_name}: $"))
        shopping_cart.append((item_name, price))  # Store the item and price as a tuple
    
    total = calculate_total_cost(shopping_cart)
    
    print(f"\nThe total cost of your purchases is: ${total:.2f}")

if __name__ == "__main__":
    main()
