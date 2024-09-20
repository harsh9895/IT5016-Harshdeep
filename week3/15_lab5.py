def student_info():
# Python cannot index integers, so we can input as string for this task
    studentID = input("Enter your student ID: ")
    student_firstName = input("Enter your first name: ")
    student_lastName = input("Enter your last name: ")
    university = input("Which university do you attend?: ").lower()
# Check if both "whitecliffe" and "college" are in the university input
    if "whitecliffe" in university and "college" in university:
# Create username from the first 2 characters of studentID and the 
# first 3 characters of student_lastName
     username = studentID[:2] + student_lastName[:3]
     print("Welcome to Whitecliffe College! Your username is", username)
    else:
     print("Please have your university generate your username.")

def main():
    student_info()
# Directly call the main function
main()