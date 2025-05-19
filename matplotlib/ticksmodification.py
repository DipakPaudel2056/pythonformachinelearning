from matplotlib import pyplot as plt

month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep","Oct", "Nov", "Dec"]

months = range(12)
conversion = [0.05, 0.08, 0.18, 0.28, 0.4, 0.66, 0.74, 0.78, 0.8, 0.81, 0.85, 0.85]

plt.xlabel("Months")
plt.ylabel("Conversion")



# Your work here
ax = plt.subplot() #we must create a subplot to be able to modifuy the 
ax.set_xticks(months) #here we are setting the x-axis as the months list
ax.set_xticklabels(month_names) #here we are setting the names from the name list
ax.set_yticks([0.10,0.25,0.5,0.75])
ax.set_yticklabels(["10%","25%","50%",'75%']) #we are labeling the y-ticks 
plt.show()