from matplotlib import pyplot as plt

past_years_averages = [82, 84, 83, 86, 74, 84, 90]
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006]
error = [1.5, 2.1, 1.2, 3.2, 2.3, 1.7, 2.4]

# Make your chart here
plt.figure(figsize=(10,8))
plt.bar(range(len(years)),past_years_averages,yerr=error,capsize=5) #created bar chart 
plt.title('Final Exam Averages') #setting title of the chart
plt.xlabel("Year") #creating x labels
plt.ylabel("Test average") #creating y labels
plt.axis([-0.5,6.5,70,95]) #setting axis
ax = plt.subplot() #creating axes object to work with the ticks
ax.set_xticks(range(len(years)))
ax.set_xticklabels(years)
plt.savefig("my_bar_chart.png") #saving the result in png file
plt.show()
