magnitude = float(input("Please enter magnitude of the earthquake:"))
if magnitude >= 10:
   print("\nThe earthquake is Meteoric""\n\n")
elif (magnitude >= 8 and magnitude <10):
   print("\nThe earthquake is Great""\n\n")
elif (magnitude >= 7 and magnitude <8):
   print("\nThe earthquake is Major""\n\n") 
elif (magnitude >= 6 and magnitude <7):
   print("\nThe earthquake is Strong""\n\n") 
elif (magnitude >= 5 and magnitude <6):
   print("\nThe earthquake is Moderate""\n\n") 
elif (magnitude >= 4 and magnitude <5):
   print("\nThe earthquake is Light""\n\n") 
elif (magnitude >= 3 and magnitude <4):
   print("\nThe earthquake is Minor""\n\n") 
elif (magnitude >= 2 and magnitude <3):
   print("\nThe earthquake is Very minor""\n\n")
else: 
   print("\nThe earthquake is Micro""\n\n")

# Testing
'''
print("My assertions are:"
"\nmagnitude = 5.7, output = Moderate"
"\nmagnitude = 0.0, output = Micro"
"\nmagnitude = 11, output = Meteoric")
'''