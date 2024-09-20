def multiplication_table(number, up_to=10):
    """Generate and Display a Multiplication Table using a For Loop."""
    print(f"MUltiplicaion Table for {number}:")
    for i in range(1, up_to + 1):
        print(f"{number} x {i} = {number * i}")

#Generate a multiplication table for the number 5
multiplication_table(int(input("Enter a number:")))