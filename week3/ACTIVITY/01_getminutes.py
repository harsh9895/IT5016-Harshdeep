def get_minutes(hours , minutes): 
    total = hours * 60 + minutes 
    return total


hours = float(input("Enter hours"))
minutes = float(input("Enter minutes"))
total_minutes = get_minutes(hours,minutes)
print(total_minutes)

# total_minutes = get_minutes(3,44)
# print(total_minutes)
 
     