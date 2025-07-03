import numpy as np
from scipy.stats import ttest_1samp
import matplotlib.pyplot as plt

prices = np.genfromtxt('prices.csv')

# print prices:
print(prices)
# calculate prices_mean and print it out:
prices_mean = np.mean(prices)
print(prices_mean)
# after printing i found that the mean is 980.0 which is slightly less than 1000
# we want to run a one-sample t-tes with following null and alternative hypotheses:
# a. null: the average cost of order is 1000 rupees
# b. alternative: the avergage cost of orrder is not 1000 rupees

# use ttest_1samp to calculate pval
tstat, pval = ttest_1samp(prices, 1000)
# print pval
print(pval)
# plot the histogram to show the relation 
plt.hist(prices)
plt.show()