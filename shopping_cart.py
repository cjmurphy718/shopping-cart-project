# shopping_cart.py
# Read CSV
import os
csv_filepath = os.path.join(os.path.dirname(__file__), "data", "products.csv")
from pandas import read_csv
products_df = read_csv(csv_filepath)
#print(products_df.head())
#print(type(products_df))
#print(products_df.columns)



#Import Products

# chosen_id = input("Please input a product identifier: ")
# print(chosen_id)

#Lookup Product
# matching_product = [product for product in products if str(product["id"]) == str(chosen_id)]

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71
