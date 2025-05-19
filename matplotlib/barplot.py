# till now we have only examined about the line chart we want to compare the new findings in other chart as well
#here we will be playing around with some bar chart

from matplotlib import pyplot as plt

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales =  [91, 76, 56, 66, 52, 27]

plt.bar(range(len(drinks)), sales) #we use plt.bar method to create bar chart
#create your ax object here
ax = plt.subplot()
ax.set_xticks(range(len(drinks)))
ax.set_xticklabels(drinks)
plt.show()