import pandas as pd

inventory = pd.read_csv("inventory.csv")

staten_Island = inventory[:10]
product_request = staten_Island['product_description']

seed_request = inventory[(inventory.location == "Brooklyn") & (inventory.product_type == "seeds")]

in_stock = lambda inventory : True if inventory > 10 else False
inventory['in_stock'] = inventory.quantity.apply(in_stock)
inventory['total_value'] = inventory.apply(lambda row: row.price * row.quantity, axis = 1)
combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type,
                     row.product_description)
inventory['full_description'] = inventory.apply(combine_lambda,axis=1)
print(inventory)
