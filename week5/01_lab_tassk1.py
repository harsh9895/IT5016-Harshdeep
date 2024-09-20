"""
collect the information
Author: Muskan

"""

def collect_user_data(id_counter):
    

    # prompt user input
   print("enter user information:")
   name = (input("enter the user name "))
   age = int(input("enter the user age "))
   email = (input("enter the user email"))


   # generate unique id:

   id_counter = id_counter + 1


   # display the user information

   print("\nuser information:")
   print(f"Name : {name}")
   print(f"Age :{age}")
   print(f"Email : {email}")
   print(f"unique_id : {id_counter}")

collect_user_data(5000)
 
 


    











                  
            




      






