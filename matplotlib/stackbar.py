from matplotlib import pyplot as plt

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales1 =  [91, 76, 56, 66, 52, 27]
sales2 = [65, 82, 36, 68, 38, 40]
plt.bar(range(len(drinks)),sales1)
plt.bar(range(len(drinks)),sales2,bottom=sales1) #the trick behind the stacked bar is bottom keyword here we are putting sales1 as the bottom of the bar plot 
plt.legend(['Location 1','Location 2'])
plt.show()