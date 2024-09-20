''' CALCULATOR '''

def add(num1, num2):
    sum = num1 + num2 
    print("Answer: ", sum)
def subtract(num1, num2):
    sum = num1 - num2
    print("Answer: ", sum)
def divide(num1, num2):
    sum = num1 / num2
    print("Answer: ", sum)
def multiply(num1, num2):
    sum = num1 * num2
    print("Answer: ", sum)

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
choice = int(input("What would you like do with these numbers? Enter the corresponding number.\n1.Add\n2.Subtract\n3.Divide\n4.Multiply\nYour choice: "))
if choice == 1:
   add(num1, num2)
elif choice == 2:
   subtract(num1, num2)
elif choice == 3:
   divide(num1, num2)
elif choice == 4:
   multiply(num1, num2)
else:
   print("Did not recognise that input.")