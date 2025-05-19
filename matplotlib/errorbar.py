from matplotlib import pyplot as plt

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
ounces_of_milk = [6, 9, 4, 0, 9, 0]
error = [0.6, 0.9, 0.4, 0, 0.9, 0]

# the trick behind the error bar is it takes the yerr keyword that gets the errot matrix and plot the error plot in the given chart and capsize is the size of the horizontal cap that we are presenting in the error bar
plt.bar(range(len(drinks)),ounces_of_milk,yerr=error,capsize=5)
plt.xticks(range(len(drinks)), drinks, rotation=45, ha='right')
plt.show()