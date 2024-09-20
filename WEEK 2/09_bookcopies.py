



# price = (float(input("enter number of copies:")) * 24.95) * 0.40
# price = (int(input("enter number of copies:")) * 24.95) * 0.40
'''
print = ("price")

shipping = 3 + 0.75 * float(input("enter additional copies:"))
print = (shipping)

wholesale_cost = price + shipping

print("your whole sale cost is $",wholesale_cost,sep="" )
'''

# book = float(input("input book price: "))
# discount = (40/100) * book
# total_books = 60
# first_shipping = 3
# rest_of_shipping = 0.75
# rest_of_books = total_books - 1

# discounted_price_book = book - discount
# total_books = discounted_price_book * total_books

# shipping = first_shipping + (rest_of_shipping * rest_of_books)

# sum = shipping + total_books
# print(sum)




# input
book_cover_price = 24.95
discount = 40/100
copies = 60

# process
book_discount_price = book_cover_price * discount

# book price after discount
unit_price = book_cover_price - book_discount_price

total = unit_price * copies

shipping = 3 + 0.75 * (copies -1)

grand_total = total + shipping
print(grand_total)










