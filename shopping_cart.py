# shopping_cart.py
# Read CSV
import os
csv_filepath = os.path.join(os.path.dirname(__file__), "data", "products.csv")
from pandas import read_csv
products_df = read_csv(csv_filepath)


#print(products_df.head())
#print(type(products_df))
#print(products_df.columns)




#Import and Lookup Product
chosen_ids =[]
total_price = 0 
while True:
    chosen_id = (input("Please input a product identifier, or DONE if there are no more products: "))
    chosen_id = chosen_id.upper()
    if chosen_id == "DONE":
        break
    else:
       chosen_ids.append(chosen_id)


#Intro Messages
#from datetime import date
#today = date.today()
#today_2 = today.strftime("%B %d, %Y")
from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
# Help from https://www.programiz.com/python-programming/datetime/current-datetime

print("------")
print("Thank you for shopping at Carol's Grocers!")
print("www.carolsgrocers.com")
print("-----")
print("Checkout at:", " ", dt_string)
print("Itemized Receipt:")

#When Done, Total Price

for chosen_id in chosen_ids:
    matching_product = [product for index, product in products_df.iterrows() if str((product["id"])) == str(chosen_id)]
    total_price = total_price + matching_product[0]["price"]
    print(matching_product[0]["name"] + " " +"(" + str(matching_product[0]["price"]) + ")")
print("-----")
print("Subtotal:" + " " + str(total_price))


sales_tax = (total_price * .0875)
total_amount = (total_price + sales_tax)
print("Sales Tax: ", sales_tax)
print("Grand Total: ", total_amount)