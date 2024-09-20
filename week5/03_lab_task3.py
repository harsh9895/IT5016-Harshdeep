
def categorize_request(total_amount):

    if total_amount < 150:
        category = "low"
        recommendation = "proceed with standard processing."
    else:
        category = "high"
        recommendation = "review for potential discounts."


    print("\nRequest summary:")
    print(f"total amount : ${total_amount:.2f}")
    print(f"category:{category}")
    print(f"recommendation:{recommendation}")


    return category, recommendation

total_amount = float(input("enter your total amount:"))

categorize_request(total_amount) 









