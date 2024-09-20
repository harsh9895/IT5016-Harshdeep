name = input("enter your name ")
age = input("enter your age")
print("hello, ",name, ".you are", age," years old", sep="")
# fstrings
print(f"hello, {name}. you are {age} years old.")


# pi = 3.141592653589
formatted_pi = f"value of pi to 2 decimal places:  {pi: .2f}"
print(formatted_pi)

salary = float(input("enteryour weekly salary"))
print(f"your weekly salary is ${salary: .2f}")

# a = 15
# b = 10
# result = f"the result of {a} multiplied by {b} is { a * b}"
# print(result)

name = {"muskan"}
age = {19}
address ={"121 queen street"}
info = f"""
name: {"sneha"}
age :{20}
address: {"6 te whitinga lane"}
"""

print(info)
