import matplotlib.pyplot as plt


x = [121,121,122,12,1122,1221,1221,1221]
y1 = [122,3332,322,33,2334,233,223,23423]
y2 = [3,4,5,6,7,7,8,8]

plt.plot(x,y1,color="pink",marker="o")
plt.plot(x,y2,color="gray",marker="o")
plt.xlabel('Amazing X-axis')
plt.ylabel('Incredible Y-axis')
plt.title("Two lines on One Graph")
plt.legend(["Y2","Y1"],loc=4)
plt.show()