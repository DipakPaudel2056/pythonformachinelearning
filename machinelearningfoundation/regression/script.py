x = [1, 2, 3]
y = [5, 1, 3]

#y = x
m1 = 1
b1 = 0

#y = 0.5x + 1
m2 = 0.5
b2 = 1

y_predicted1 = [m1*x_item + b1 for x_item in x]
y_predicted2 = [m2*x_item + b2 for x_item in x]
total_loss1 = 0
for i in range(len(y_predicted1)):
  total_loss1 += (y[i] - y_predicted1[i])**2
total_loss2 = 0
for i in range(len(y_predicted2)):
  total_loss2 += (y[i] - y_predicted2[i])**2
print(total_loss1,total_loss2)
better_fit=2


# here we are trying to find the better slope and the intercept value for to be used in the regression model using linear regeression model 
# we have examined the loss1 and the loss2 using the loss finding formula which is the sum of (y-value - predicted_yvalue)^2

# two loss algorithm showed that the second line had less loss that's why we used the second m,b combination