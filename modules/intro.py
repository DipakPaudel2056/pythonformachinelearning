# when we are writing code for ourself we often time make it in such a way that we donot have to repeat ourselves. They can be bundeled in file or in a set of files which are also called as module
from datetime import datetime
import random
currenttime = datetime.now()

# Import random below:
import random

# Create random_list below:
random_list = [random.randint(1,100) for x in range(101)]


# Create randomer_number below:
randomer_number = random.choice(random_list)

# Print randomer_number below:
print(randomer_number)

# codecademy project on module
import codecademylib3_seaborn
from matplotlib import pyplot as plt
import random
numbers_a = range(1,13)
numbers_b =random.sample(range(1000),12)
print(numbers_b)
# Add your code below:
plt.plot(numbers_a, numbers_b)
plt.show()