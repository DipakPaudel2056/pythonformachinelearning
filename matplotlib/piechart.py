# we also want to see how the pie chart are created using matplot lib for this we use the method called .pie 
from matplotlib import pyplot as plt
import numpy as np

payment_method_names = ["Card Swipe", "Cash", "Apple Pay", "Other"]
payment_method_freqs = [270, 77, 32, 11]

#make your pie chart here
plt.pie(payment_method_freqs) #to create a basic pie with the help of payment method frequencies
plt.axis('equal')


# lets add the labels in the pie chart
plt.pie(payment_method_freqs,labels=payment_method_names,autopct='%0.1f%%')
plt.axis('equal')
plt.show()