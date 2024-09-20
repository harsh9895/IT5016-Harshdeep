def password_attempt_system():
    """A Simple password attempt system using while loop."""
    correct_password = "python123"
    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        entered_password = input("Enter Your Password:")
        if entered_password == correct_password:
            print ("Access Granted!")
            break
        else:
            attempts += 1
            print(f"Incorrect Password. You have {max_attempts - attempts} attempts left.")

        if attempts == max_attempts:
            print ("Access Denied. You have used all your attempts.")

#Run the password attempt system
password_attempt_system()

