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
total_price = 0 
while True:
    chosen_id = (input("Please input a product identifier, or DONE if there are no more products: "))
    chosen_id = chosen_id.upper()
    if chosen_id == "DONE":
        break
    else:
        matching_product = [product for index, product in products_df.iterrows() if str((product["id"])) == str(chosen_id)]
    #print(type(matching_product))
    total_price = total_price + matching_product[0]["price"]
    print("Selected Product:" + matching_product[0]["name"] + " " + str(matching_product[0]["price"]))

#When Done, Total Price
print("Total Price:" + str(total_price))

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71
