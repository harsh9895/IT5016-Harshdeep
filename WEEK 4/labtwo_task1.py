# Initialize an empty dictionary
students = {}

# Number of students to add
num_students = int(input("How many students do you want to add? "))

# Loop to get student registration numbers and names
for i in range(num_students):
    reg_number = input("Enter the student's registration number: ")
    first_name = input("Enter the student's first name: ")
    
    # Add the student to the dictionary
    students[reg_number] = first_name

# Display the final dictionary
print("\nStudent Data:")
print(students)
