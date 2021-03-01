''' script to draw a sine wave '''

import numpy as np #number functions
import matplotlib.pyplot as plt #plotting functions
import os #file and folder functions

x = np.linspace(-6,6,100) #get x values for the points
y = np.sin(x) #get the corresponding y values 

plt.clf() #clear current plot (if there is one)
plt.plot(x,y) #plot the points
plt.xlabel('x (radians)') #add xlabel
plt.ylabel('sin(x)')  #add ylabel
plt.savefig(os.path.join('outputs','sine.png')) #export graph as png
