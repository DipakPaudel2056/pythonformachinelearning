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
plt.show()

# lets see the tutorial from codecademy
time = [0, 1, 2, 3, 4]
revenue = [200, 400, 650, 800, 850]
costs = [150, 500, 550, 550, 560]

plt.plot(time,revenue,color='purple',linestyle='--')
plt.plot(time,costs,color='#82edc9',marker='s')
plt.show()