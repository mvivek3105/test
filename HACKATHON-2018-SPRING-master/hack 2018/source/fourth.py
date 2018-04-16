#importing numpy
import numpy as np
#Assigning to x which is refered as most occured one in the list
x=np.random.randint(0, 20, 15)
#printing the given list
print("Given List:")
#printing the most occured one
print(x)
print("Most repeated frequent value in the List:")
print(np.bincount(x).argmax())