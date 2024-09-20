
def calculate_total_amount():

    # prompt the users to input prices:
    item_details = []
    prices = []
    total_amount = 0
    
    while True:
        item_detail =str(input("item name  (finish to end)"))
        if item_detail.lower() == 'finish':
            break
        else:
            price =int(input("enter price"))
            item_details.append(item_detail)
            prices.append(price)

    total_amount += price
                                                                                                                                                            
    print(total_amount)



calculate_total_amount()
        


        

    


