# in this project we are going to find how much time the customer are spending in the site
import pandas as pd
visits = pd.read_csv('panda/multipletable/visits.csv',
                        parse_dates=[1])
checkouts = pd.read_csv('panda/multipletable/checkout.csv',
                        parse_dates=[1])
v_to_c = pd.merge(visits,checkouts)
v_to_c['time'] = v_to_c.checkout_time - v_to_c.visit_time
print(v_to_c.time.mean()) #it is going to be 15 minutes