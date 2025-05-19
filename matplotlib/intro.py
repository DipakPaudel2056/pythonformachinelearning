# importing matplotlib
import matplotlib
print(matplotlib.__version__)

# my first chart
from matplotlib import pyplot as plt
# get x-axis values in array
#get y-axis values in array
# use plt method to plot the line
x = [0,1,2,3,4]
y = [0,1,4,9,16]

# we can also plot a different graph here for example if i have z to compare her
z = [0,1,8,27,64]
plt.plot(x,y)
plt.plot(x,z)

# lets see the tutorial from codecademy
time = [0, 1, 2, 3, 4]
revenue = [200, 400, 650, 800, 850]
costs = [150, 500, 550, 550, 560]

plt.plot(time,revenue,color='purple',linestyle='--')
plt.plot(time,costs,color='#82edc9',marker='s')

# here we donot have the control on how much of zoom is required on the chart
# to deal with this issue we want to use .axis method and pass min-x,max-x,min-y,max-y 

# we can also make the change in the name of the x-axis y-axis and the title to do so we use
#.xlabel
#.ylabel
#.title method
plt.plot(time,revenue)
plt.xlabel('time')
plt.ylabel('revenue')
plt.title('revenue vs time')


# subplot are the plots that are plotted in the same figure and it takes the parameter that defins the x value, y-value and the order of the plot
# for example if we want to plot 2 plot side by side which is in the [1,2] matrix and the other parameter is 1, or 2 based on the order

# lets display 2plots in the same figure i am trying to plot time vs rev in 1 and rev vs costs in 2
plt.subplot(1,2,1)
plt.plot(time,revenue)

plt.subplot(1,2,2)
plt.plot(costs,revenue, "o")

plt.show()
