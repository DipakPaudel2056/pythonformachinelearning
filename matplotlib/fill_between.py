# we may want to include the error aspect in the line chart as well, in this case the handy method is fill_between method
# fill_between method takes 3 attributes, x-axis value[list], lower-y[list] bound and the upper y-bound[list] and the alpha[float] alpha is the opacity
from matplotlib import pyplot as plt

months = range(12)
month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
revenue = [16000, 14000, 17500, 19500, 21500, 21500, 22000, 23000, 20000, 19500, 18000, 16500]

plt.plot(months,revenue) #it creates a line chart with revenue vs months
ax = plt.subplot() #creating ax axes object to work with the plot
ax.set_xticks(range(len(month_names))) #creating x ticks to be equal to the index of months name
ax.set_xticklabels(month_names) #labeling the x ticks
y_lower = [i - 0.1 * i for i in revenue] #creating y-lower bound with 10% error margin
y_upper = [i + 0.1 * i for i in revenue] #creating y-upper bound with 10% error margin
plt.fill_between(months,y_lower,y_upper,alpha=0.2) #using fill_between method to display the error range of the line chart
plt.show() #displaying the chart