import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import binom_test

monthly_report = pd.read_csv('monthly_report.csv')

#print the head of monthly_report:
print(monthly_report.head())

#calculate and print sample_size:
sample_size = len(monthly_report)
print(sample_size)

#calculate and print num_purchased:
num_purchased = np.sum(monthly_report.purchase == 'y')
print(num_purchased)


# simulating randomness

#simulate one visitor:
one_visitor = np.random.choice(['y','n'],size=1,p=[0.1,0.9])
print(one_visitor)

#simulate 500 visitors:
simulated_monthly_visitors = np.random.choice(['y','n'],size=500,p=[0.1,0.9])
print(simulated_monthly_visitors)


# simulating null distribution II
null_outcomes = []

#start for loop here:
for i in range(10000):
  simulated_monthly_visitors = np.random.choice(['y', 'n'], size=500, p=[0.1, 0.9])

  num_purchased = np.sum(simulated_monthly_visitors == 'y')
  null_outcomes.append(num_purchased)



#calculate the minimum and maximum values in null_outcomes here:

null_min = np.min(null_outcomes)
null_max = np.max(null_outcomes)
print(null_min,null_max)

#plot the histogram here:
plt.hist(null_outcomes)
plt.axvline(41, color = 'r')
plt.show()


# confidence interval 
null_90CI = np.percentile(null_outcomes,[5,95])
print(null_90CI)


# calculating one sided p-value
#calculate the p-value here:
null_outcomes = np.array(null_outcomes)
p_value = np.sum(null_outcomes <= 41)/len(null_outcomes)
print(p_value)


# calculating 2 sided p-value
null_outcomes = np.array(null_outcomes)
p_value = np.sum((null_outcomes <= 41) | (null_outcomes >= 59))/len(null_outcomes) 
print(p_value)


# now the scipy comes to rescue to bunle of all this jargain 
# calculate p_value_2sided here:
p_value_2sided = binom_test(41,n=500,p=0.1)
# calculate p_value_1sided here:
p_value_1sided = binom_test(41,n=500,p=0.1,alternative="less")
print(p_value_2sided)
print(p_value_1sided)