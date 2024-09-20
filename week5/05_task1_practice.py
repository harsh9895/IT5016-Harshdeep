"""
collecting user information 
Author : muskan 
"""

def collect_user_data(id_counter):
    # prompt user input:
    print("collect user information")
    user_name = (input("enter user name"))
    user_age = (input("enter user name "))
    user_email_Id = (input("enter user email"))

    # generate unique id

    id_counter = id_counter + 1

    # display of user information

    print("\nuser information")
    print(f"Name : {user_name}")
    print(f"age : {user_age}")
    print(f"email : {user_email_Id}")
    print(f"unique_id : {id_counter}")

collect_user_data(5000)




